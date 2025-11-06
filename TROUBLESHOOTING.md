# Troubleshooting Guide

## Issue 1: Session Not Persisting (Need to login every time)

### Problem
Getting 404 errors: `GET /api/auth/verify ... 404 Not Found`

### Solution

**Step 1: Check if Backend is Running**
```bash
cd backend
python main.py
```

You should see:
```
✅ Connected to MongoDB: lernova_db
✅ Lernova API started successfully
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Step 2: Check if MongoDB is Running**
```bash
# Windows
mongod --dbpath C:\data\db

# Linux/Mac
mongod --dbpath /data/db
```

**Step 3: Test Auth Endpoint Manually**
Open browser and go to:
```
http://localhost:8000/api/auth/verify?session_token=test
```

Should return 401 (not 404). If 404, backend isn't running properly.

**Step 4: Use Guest Mode**
If backend issues persist, use "Continue as Guest" - this works offline.

---

## Issue 2: Websites Not Loading (Blank Screen)

### Problem
After searching, webview shows blank screen

### Solution

**Step 1: Open DevTools for Webview**
The webview now auto-opens DevTools. You'll see TWO DevTools windows:
1. Main app DevTools (for React)
2. Webview DevTools (for loaded websites)

**Step 2: Check Webview Console**
Look in the WEBVIEW DevTools (second window) for errors like:
- `net::ERR_NAME_NOT_RESOLVED` - DNS issue
- `net::ERR_INTERNET_DISCONNECTED` - No internet
- `net::ERR_CERT_AUTHORITY_INVALID` - SSL issue

**Step 3: Check Main Console**
In the MAIN DevTools, look for:
```
Loading URL in webview: https://...
Webview ready for tab: ...
```

If you don't see these, the webview isn't initializing.

**Step 4: Test with Simple URL**
Try loading: `https://example.com`

If this works but search doesn't, the search engine URL might be wrong.

**Step 5: Check Internet Connection**
```bash
ping google.com
```

---

## Issue 3: Backend 404 Errors

### Symptoms
```
INFO: 127.0.0.1:xxxxx - "GET /api/auth/verify?session_token=... HTTP/1.1" 404 Not Found
```

### Root Causes

**Cause 1: Backend Not Running**
- Solution: Start backend with `python main.py`

**Cause 2: Wrong Port**
- Backend should run on port 8000
- Check `.env` file for `PORT=8000`

**Cause 3: Routes Not Loaded**
- Check `backend/main.py` has: `app.include_router(auth.router, prefix="/api/auth")`

**Cause 4: MongoDB Not Connected**
- Check MongoDB is running
- Check connection string in `.env`

### Quick Fix
1. Stop backend (Ctrl+C)
2. Check MongoDB is running
3. Restart backend: `python main.py`
4. Restart frontend: `npm run electron:dev`

---

## Issue 4: DevTools Not Showing

### Enable DevTools

**For Main App:**
Uncomment in `electron/main.cjs`:
```javascript
newWindow.webContents.openDevTools()
```

**For Webview:**
Already enabled automatically when webview attaches.

**Manual Open:**
- Press `F12` or `Ctrl+Shift+I`
- Right-click → Inspect Element

---

## Issue 5: CORS Errors

### Symptoms
```
Access to XMLHttpRequest blocked by CORS policy
```

### Solution
Check `backend/main.py`:
```python
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
```

Should include `http://localhost:5173`

---

## Quick Diagnostic Checklist

Run through this checklist:

- [ ] MongoDB is running (`mongod` command)
- [ ] Backend is running (`python main.py` in backend folder)
- [ ] Backend shows "✅ Connected to MongoDB"
- [ ] Backend is on port 8000
- [ ] Frontend is running (`npm run electron:dev`)
- [ ] Can see login screen
- [ ] Internet connection working
- [ ] DevTools are open (F12)
- [ ] No red errors in main console
- [ ] Webview DevTools show website console

---

## Common Error Messages

### "Auth endpoint not found. Is the backend running on http://localhost:8000?"
**Fix:** Start the backend server

### "Failed to save history: Network Error"
**Fix:** Backend not running or wrong API_URL

### "WebView failed to load: ERR_NAME_NOT_RESOLVED"
**Fix:** Check internet connection or URL format

### "Session verification failed: 404"
**Fix:** Backend not running or auth routes not loaded

---

## Environment Variables

Create `.env` file in backend folder:
```env
GROQ_API_KEY=your_groq_api_key_here
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=lernova_db
PORT=8000
CORS_ORIGINS=http://localhost:5173
```

Create `.env` file in frontend folder:
```env
VITE_API_URL=http://localhost:8000
```

---

## Testing Steps

### Test 1: Backend Health
```bash
curl http://localhost:8000/
```
Should return JSON with "Lernova Browser API"

### Test 2: Auth Endpoint
```bash
curl http://localhost:8000/api/auth/verify?session_token=test
```
Should return 401 (not 404)

### Test 3: MongoDB Connection
```bash
mongosh
use lernova_db
db.users.find()
```
Should connect without errors

---

## Still Not Working?

1. **Clear all data and restart:**
   ```bash
   # Stop everything
   # Clear localStorage in browser (F12 → Application → Local Storage → Clear)
   # Restart MongoDB
   mongod --dbpath /path/to/data
   # Restart backend
   cd backend && python main.py
   # Restart frontend
   cd frontend && npm run electron:dev
   ```

2. **Check logs:**
   - Backend terminal for errors
   - Main DevTools console (F12)
   - Webview DevTools console (second window)

3. **Use Guest Mode:**
   - Click "Continue as Guest"
   - This bypasses authentication
   - Test if websites load

4. **Report the error:**
   - Copy full error message from console
   - Note which step failed
   - Share backend terminal output
