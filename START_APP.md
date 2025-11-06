# How to Start the Application

## Prerequisites Check

Before starting, ensure you have:
- ✅ MongoDB installed and running
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ Backend dependencies installed
- ✅ Frontend dependencies installed

---

## Step-by-Step Startup

### Step 1: Start MongoDB

**Windows:**
```bash
# Open Command Prompt as Administrator
mongod --dbpath C:\data\db
```

**Linux/Mac:**
```bash
sudo mongod --dbpath /data/db
```

**Keep this terminal open!** You should see:
```
[initandlisten] waiting for connections on port 27017
```

---

### Step 2: Start Backend

**Open a NEW terminal:**

```bash
cd e:\hackkarnatak\backend
python main.py
```

**Expected output:**
```
Loaded GROQ_API_KEY: gsk_...
INFO:     Started server process
INFO:     Waiting for application startup.
✅ Connected to MongoDB: lernova_db
✅ Lernova API started successfully
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Keep this terminal open!**

---

### Step 3: Start Frontend (Electron)

**Open a NEW terminal:**

```bash
cd e:\hackkarnatak\frontend
npm run electron:dev
```

**Expected output:**
```
VITE v4.x.x  ready in xxx ms
➜  Local:   http://localhost:5173/
```

Then Electron window should open automatically.

**Keep this terminal open!**

---

## What You Should See

1. **Electron window opens**
2. **Login screen appears** with options:
   - Sign up
   - Login
   - Continue as Guest
3. **Two DevTools windows** (can close the webview one if not debugging)

---

## Quick Test

After login:

1. **Test Search:**
   - Type: `test query`
   - Press Enter
   - Should open Google search

2. **Test Direct URL:**
   - Type: `example.com`
   - Press Enter
   - Should load example.com

3. **Check Console:**
   - Press F12
   - Look for: "Loading URL in webview: ..."
   - Should see no red errors

---

## If Something Goes Wrong

### Backend Won't Start

**Error: "ModuleNotFoundError"**
```bash
cd backend
pip install -r requirements.txt
```

**Error: "MongoDB connection failed"**
- Check MongoDB is running (Step 1)
- Check MongoDB is on port 27017

**Error: "Address already in use"**
- Port 8000 is taken
- Kill the process: `netstat -ano | findstr :8000`
- Or change port in backend/.env

---

### Frontend Won't Start

**Error: "Cannot find module"**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Error: "Port 5173 already in use"**
- Kill the process or change port in vite.config.mjs

---

### Electron Window Opens But Blank

1. **Check browser console (F12)**
2. **Look for errors**
3. **Check backend is running**
4. **Try guest mode**

---

## Normal Startup Sequence

You should have **3 terminals open**:

```
Terminal 1: MongoDB
[initandlisten] waiting for connections

Terminal 2: Backend
✅ Lernova API started successfully
INFO: Uvicorn running on http://127.0.0.1:8000

Terminal 3: Frontend
VITE v4.x.x ready
➜  Local: http://localhost:5173/
```

Plus **1 Electron window** with the app.

---

## Stopping the Application

**Proper shutdown:**

1. Close Electron window
2. Terminal 3 (Frontend): Press `Ctrl+C`
3. Terminal 2 (Backend): Press `Ctrl+C`
4. Terminal 1 (MongoDB): Press `Ctrl+C`

**Or just close all terminals** (not recommended but works)

---

## Development Mode Features

When running in dev mode:

- ✅ Hot reload (code changes auto-refresh)
- ✅ DevTools auto-open
- ✅ Detailed console logging
- ✅ Source maps for debugging

---

## Production Build

To create a production build:

```bash
# Build frontend
cd frontend
npm run build

# Build Electron app
npm run electron:build
```

This creates an executable in `frontend/dist-electron/`

---

## Environment Variables

Make sure these files exist:

**backend/.env:**
```env
GROQ_API_KEY=your_key_here
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=lernova_db
PORT=8000
CORS_ORIGINS=http://localhost:5173
```

**frontend/.env:**
```env
VITE_API_URL=http://localhost:8000
```

---

## First Time Setup

If this is your first time running:

```bash
# 1. Install backend dependencies
cd backend
pip install -r requirements.txt

# 2. Install frontend dependencies
cd ../frontend
npm install

# 3. Start MongoDB (keep running)
mongod --dbpath C:\data\db

# 4. Start backend (new terminal)
cd backend
python main.py

# 5. Start frontend (new terminal)
cd frontend
npm run electron:dev
```

---

## Troubleshooting

If you encounter issues, see `TROUBLESHOOTING.md` for detailed solutions.

Common issues:
- MongoDB not running → Start MongoDB first
- Backend 404 errors → Backend not running
- Blank webview → Check console for errors
- Session not persisting → Backend/MongoDB issue

---

## Success Indicators

✅ **MongoDB:** "waiting for connections on port 27017"
✅ **Backend:** "✅ Lernova API started successfully"
✅ **Frontend:** Electron window opens with login screen
✅ **Webview:** Can load websites after login
✅ **Console:** No red errors in F12 console

---

**Ready to go!** 🚀
