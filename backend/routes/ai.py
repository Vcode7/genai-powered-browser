from fastapi import APIRouter, HTTPException
from models import AIRequest, AIResponse, SummarizeRequest, QuestionRequest, TTSRequest
from pydantic import BaseModel
from typing import List, Dict
from services.langchain_utils import langchain_service
from services.eleven_labs import eleven_labs_client
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


class HighlightRequest(BaseModel):
    topic: str
    pageTitle: str
    pageUrl: str
    elements: List[Dict]

@router.post("/chat", response_model=AIResponse)
async def chat(request: AIRequest):
    """General AI chat endpoint"""
    try:
        # Generate text response
        text_response = await langchain_service.general_chat(
            query=request.query,
            context=request.context
        )
        
        # Generate voice response
        audio_base64 = await eleven_labs_client.text_to_speech(text_response)
        
        return AIResponse(
            text=text_response,
            audio_base64=audio_base64
        )
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize", response_model=AIResponse)
async def summarize(request: SummarizeRequest):
    """Summarize webpage content"""
    try:
        # Generate summary
        summary = await langchain_service.summarize_content(
            content=request.content,
            url=request.url
        )
        
        # Generate voice
        audio_base64 = await eleven_labs_client.text_to_speech(summary)
        
        return AIResponse(
            text=summary,
            audio_base64=audio_base64
        )
    except Exception as e:
        logger.error(f"Summarize error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/question", response_model=AIResponse)
async def answer_question(request: QuestionRequest):
    """Answer question based on context"""
    try:
        # Generate answer
        answer = await langchain_service.answer_question(
            question=request.question,
            context=request.context,
            url=request.url
        )
        
        # Generate voice
        audio_base64 = await eleven_labs_client.text_to_speech(answer)
        
        return AIResponse(
            text=answer,
            audio_base64=audio_base64
        )
    except Exception as e:
        logger.error(f"Question error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tts", response_model=AIResponse)
async def text_to_speech(request: TTSRequest):
    """Convert text to speech"""
    try:
        audio_base64 = await eleven_labs_client.text_to_speech(
            text=request.text,
            voice_id=request.voice_id
        )
        
        return AIResponse(
            text=request.text,
            audio_base64=audio_base64
        )
    except Exception as e:
        logger.error(f"TTS error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/highlight-important")
async def highlight_important(request: HighlightRequest):
    """Analyze page content and identify important sections based on topic"""
    try:
        # Build prompt for AI
        elements_text = "\n\n".join([
            f"[ID: {el['id']}] {el['tag']}: {el['text'][:300]}"
            for el in request.elements[:50]  # Limit to first 50 elements
        ])
        
        prompt = f"""You are analyzing a webpage titled "{request.pageTitle}" to help a user research the topic: "{request.topic}".

Below are sections of the webpage with their IDs. Identify which sections are most relevant and important for understanding "{request.topic}".

Webpage sections:
{elements_text}

Task: Return ONLY a JSON array of IDs for the most important sections. Include 5-15 sections that are most relevant to the topic "{request.topic}".

Example response format: {{"important_ids": [0, 3, 7, 12]}}

Your response (JSON only):"""

        # Call AI
        response = await langchain_service.general_chat(
            query=prompt,
            context=f"Analyzing webpage: {request.pageUrl}"
        )
        
        # Parse response
        import json
        import re
        
        # Try to extract JSON from response
        json_match = re.search(r'\{.*"important_ids".*\}', response, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            important_ids = result.get('important_ids', [])
        else:
            # Fallback: try to find numbers in response
            numbers = re.findall(r'\d+', response)
            important_ids = [int(n) for n in numbers[:15]]
        
        logger.info(f"Identified {len(important_ids)} important sections for topic: {request.topic}")
        
        return {
            "success": True,
            "important_ids": important_ids,
            "topic": request.topic,
            "count": len(important_ids)
        }
        
    except Exception as e:
        logger.error(f"Highlight error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
