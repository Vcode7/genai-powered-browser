# Testing Guide - Lernova Browser

## Quick Start Testing

### Prerequisites
1. MongoDB running on `mongodb://localhost:27017`
2. Backend dependencies installed (`pip install -r backend/requirements.txt`)
3. Frontend dependencies installed (`npm install` in frontend folder)

---

## Step-by-Step Testing

### 1. Start the Application

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```
Expected output: `✅ Connected to MongoDB: lernova_db`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run electron:dev
```
Expected: Electron window opens with login screen

---

### 2. Test User Authentication

**Sign Up:**
1. Click "Don't have an account? Sign up"
2. Enter:
   - Name: Test User
   - Email: test@example.com
   - Password: test123
3. Click "Sign Up"
4. Should see browser interface with "Test User" in top-right

**Guest Mode:**
1. Click "Continue as Guest"
2. Should enter as "Guest User"

**Logout:**
1. Click user icon in top-right
2. Click "Logout"
3. Should return to login screen

---

### 3. Test History Tracking

1. Log in
2. Navigate to any website (e.g., google.com)
3. Wait for page to load completely
4. Click Settings icon
5. Go to "History" tab
6. Should see the visited page listed
7. Try searching history with keywords

**Expected:**
- URL, title, and timestamp shown
- Visit count increments on revisit
- Search filters results

---

### 4. Test Search Engine

1. Go to Settings > General
2. Change "Default Search Engine" to "DuckDuckGo"
3. Click "Save Changes"
4. Close settings
5. In URL bar, type: `test query` (not a URL)
6. Press Enter
7. Should open DuckDuckGo search results

**Test Other Engines:**
- Google
- Bing
- Brave Search
- Ecosia

---

### 5. Test Downloads

**Trigger a Download:**
1. Go to any website with downloadable files
2. Click a download link (e.g., PDF, image, software)
3. Choose save location
4. Click Downloads button (download icon in nav bar)

**Expected:**
- Download appears in list
- Progress bar shows real-time progress
- Status updates (in_progress → completed)
- File size displayed
- Timestamp shown

**Test Actions:**
- Delete individual download
- Clear completed downloads
- Watch progress update every 2 seconds

---

### 6. Test Right-Click Context Menu

**Basic Context Menu:**
1. Navigate to any webpage
2. Right-click anywhere
3. Should see menu with:
   - Inspect Element
   - Back/Forward/Reload

**Click "Inspect Element":**
- DevTools should open at clicked element

**On Text:**
1. Select some text on page
2. Right-click
3. Should see:
   - Ask AI Chat
   - Copy
   - Inspect Element

**On Links:**
1. Right-click a link
2. Should see:
   - Open Link in New Tab
   - Copy Link Address

**On Images:**
1. Right-click an image
2. Should see:
   - Save Image As...
   - Copy Image

---

### 7. Test Text Selection AI Chat

**Method 1: Context Menu**
1. Navigate to any article/webpage
2. Select interesting text (e.g., a paragraph)
3. Right-click on selection
4. Click "Ask AI Chat"

**Expected:**
- AI Chat panel opens on right
- Message appears: "Explain or help with: [selected text]"
- AI provides explanation/help
- Selected text included as context

**Method 2: Drag Selection**
1. Click and drag to select text
2. Right-click
3. Choose "Ask AI Chat"

**Test Different Selections:**
- Single word
- Sentence
- Paragraph
- Code snippet
- Technical term

---

### 8. Test localStorage & Cookies

**Session Persistence:**
1. Log in to browser
2. Visit a website that uses cookies (e.g., login to Gmail)
3. Close Electron app completely
4. Reopen app
5. Should still be logged in
6. Website cookies should persist

**Settings Persistence:**
1. Change theme to Dark
2. Change search engine to Bing
3. Close app
4. Reopen
5. Settings should be preserved

---

## Feature Checklist

Use this to verify all features work:

### Authentication
- [ ] Sign up new user
- [ ] Log in existing user
- [ ] Guest mode works
- [ ] Logout works
- [ ] Session persists after restart
- [ ] User menu shows correct info

### History
- [ ] Pages are tracked automatically
- [ ] History appears in Settings
- [ ] Visit count increments
- [ ] Search history works
- [ ] Clear history works
- [ ] Timestamps are correct

### Search Engine
- [ ] Can change in settings
- [ ] Google search works
- [ ] Bing search works
- [ ] DuckDuckGo search works
- [ ] Brave search works
- [ ] Ecosia search works
- [ ] Setting persists

### Downloads
- [ ] Downloads are tracked
- [ ] Progress shows in real-time
- [ ] Status updates correctly
- [ ] File info is accurate
- [ ] Can delete downloads
- [ ] Can clear completed
- [ ] List refreshes automatically

### Context Menu
- [ ] Right-click shows menu
- [ ] Inspect Element works
- [ ] Menu adapts to context (text/link/image)
- [ ] Navigation options work
- [ ] Copy functions work
- [ ] Save image works

### Text Selection AI
- [ ] Can select text
- [ ] "Ask AI Chat" appears in menu
- [ ] AI Chat opens with selection
- [ ] AI understands context
- [ ] Works with different text lengths
- [ ] Multiple selections work

### Cookies & Storage
- [ ] Cookies persist across sessions
- [ ] localStorage works
- [ ] Login states preserved
- [ ] Settings saved locally
- [ ] Session tokens work

---

## Common Issues & Solutions

### Issue: MongoDB connection failed
**Solution:** 
```bash
# Start MongoDB service
mongod --dbpath /path/to/data
```

### Issue: Backend not starting
**Solution:**
```bash
# Check if port 8000 is free
# Install dependencies
pip install -r backend/requirements.txt
```

### Issue: Frontend build errors
**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Issue: Context menu not showing
**Solution:**
- Ensure you're using Electron (not web browser)
- Right-click inside the webview area
- Check Electron version compatibility

### Issue: AI Chat not opening
**Solution:**
- Check backend is running
- Verify GROQ_API_KEY in .env
- Check browser console for errors

### Issue: Downloads not tracking
**Solution:**
- Ensure backend is running
- Check MongoDB connection
- Verify axios is installed in Electron

---

## Performance Testing

### Load Testing
1. Open 10+ tabs
2. Navigate to different sites
3. Check memory usage
4. Verify all tabs work

### History Testing
1. Visit 50+ different pages
2. Check history loads quickly
3. Search should be fast
4. No duplicates

### Download Testing
1. Download multiple files simultaneously
2. Check all progress bars update
3. Verify no conflicts

---

## Security Testing

### Authentication
- [ ] Passwords are hashed (check MongoDB)
- [ ] Session tokens are secure
- [ ] Can't access without login (except guest)
- [ ] Logout clears session

### Webview Security
- [ ] Context isolation enabled
- [ ] No node integration in webview
- [ ] XSS protection works
- [ ] CORS respected

---

## Browser Compatibility

Test on:
- [ ] Windows 10/11
- [ ] macOS
- [ ] Linux

---

## Final Verification

Run through this complete flow:

1. ✅ Start fresh (clear MongoDB)
2. ✅ Sign up new user
3. ✅ Browse 5 different websites
4. ✅ Check history saved
5. ✅ Change search engine
6. ✅ Download a file
7. ✅ Select text and ask AI
8. ✅ Right-click and inspect
9. ✅ Logout and login again
10. ✅ Verify all data persists

---

**If all checkboxes pass, the application is working correctly!** ✅

For issues, check:
- Backend logs
- Frontend console (F12)
- MongoDB data
- Network tab for API calls
