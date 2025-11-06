# Capacitor Debugging Guide

## Fixed Issues

The blank white screen issue has been resolved by:

1. **Updated Content Security Policy (CSP)** - Relaxed CSP in `index.html` to allow Capacitor resources
2. **Added Capacitor Initialization** - Modified `main.jsx` to properly initialize Capacitor before React renders
3. **Fixed Build Configuration** - Updated `vite.config.mjs` for better Capacitor compatibility
4. **Added Missing Plugins** - Installed `@capacitor/splash-screen` and `@capacitor/keyboard`
5. **Improved Auth Handling** - Added timeout and error handling to prevent blocking on startup

## Testing the App

### 1. Build and Sync
```bash
cd frontend
npm run build
npx cap sync android
```

### 2. Open in Android Studio
```bash
npx cap open android
```

### 3. Run on Device/Emulator
- Click the "Run" button in Android Studio
- Or use: `npx cap run android`

## Debugging Tips

### Enable Chrome DevTools for Android
1. Open Chrome and go to `chrome://inspect`
2. Connect your Android device via USB
3. Enable USB debugging on your device
4. Your app should appear in the list - click "inspect"

### Check Logcat in Android Studio
- View > Tool Windows > Logcat
- Filter by your app package: `com.aichat.browser`
- Look for JavaScript errors or Capacitor warnings

### Common Issues

#### White Screen Still Appears
1. Clear app data: Settings > Apps > AiChat Browser > Storage > Clear Data
2. Rebuild: `npm run build && npx cap sync android`
3. Check console for errors in Chrome DevTools

#### App Crashes on Startup
1. Check Logcat for native errors
2. Verify all Capacitor plugins are installed: `npm ls @capacitor`
3. Clean and rebuild in Android Studio: Build > Clean Project

#### Network Requests Failing
1. Check if backend is accessible from the device
2. Update `VITE_API_URL` in `.env` to use your computer's IP address
3. Example: `VITE_API_URL=http://192.168.1.100:8000`

## Development Workflow

### For Live Reload During Development
1. Start Vite dev server: `npm run dev`
2. Get your computer's IP address
3. Update `capacitor.config.ts`:
```typescript
server: {
  url: 'http://YOUR_IP:5173',
  cleartext: true
}
```
4. Sync: `npx cap sync android`
5. Run app - it will connect to your dev server

### For Production Build
1. Comment out the `server.url` in `capacitor.config.ts`
2. Build: `npm run build`
3. Sync: `npx cap sync android`
4. Run app

## Platform Detection

The app uses `src/utils/platform.js` to detect the platform:
- `isCapacitor()` - Returns true when running in Capacitor
- `isElectron()` - Returns true when running in Electron
- `isWeb()` - Returns true when running in browser

## Environment Variables

Create a `.env` file in the frontend directory:
```
VITE_API_URL=http://localhost:8000
```

For mobile testing, use your computer's IP:
```
VITE_API_URL=http://192.168.1.100:8000
```

## Useful Commands

```bash
# Install dependencies
npm install

# Build for production
npm run build

# Sync with Capacitor
npx cap sync

# Sync only Android
npx cap sync android

# Open Android Studio
npx cap open android

# Run on Android device
npx cap run android

# Check Capacitor doctor
npx cap doctor
```
