# 🎭 Shakespeare's Digital Quill - Frontend

A beautiful, theatrical frontend for your NanoGPT Shakespeare text generator!

## ✨ Features

- 🎨 **Elegant Shakespearean Design** - Purple gradients and theatrical themes
- 📝 **Optional Prompts** - Start with your own text or let the AI surprise you
- 🎲 **Random Length Generation** - Choose specific lengths or let it pick randomly
- ⚡ **Real-time Stats** - See generation time, tokens, and character count
- 📋 **Copy to Clipboard** - Easy sharing of generated text
- 📱 **Responsive Design** - Works beautifully on all devices

## 🚀 Quick Start

### Option 1: Direct File Opening (Simplest)
1. Make sure your backend is running:
   ```bash
   cd "d:\Neural Networks\nano_gpt\Backend"
   uvicorn main:app --reload
   ```

2. **IMPORTANT**: Add CORS support to your backend by installing:
   ```bash
   pip install fastapi-cors
   ```

3. Simply double-click `index.html` or open it in your browser!

### Option 2: Using Python HTTP Server (Recommended)
1. Start your backend API (see above)

2. In a new terminal, navigate to the Frontend folder:
   ```bash
   cd "d:\Neural Networks\nano_gpt\Frontend"
   python -m http.server 8080
   ```

3. Open your browser and go to:
   ```
   http://localhost:8080
   ```

## ⚙️ Configuration

The frontend connects to the API at `http://localhost:8000` by default.

If your backend runs on a different port, edit line 301 in `index.html`:
```javascript
const API_URL = 'http://localhost:YOUR_PORT';
```

## 🎯 How to Use

1. **Enter a Prompt** (Optional)
   - Type a starting phrase like "To be or not to be"
   - Or leave it blank for random generation

2. **Choose Length**
   - Select a specific token count
   - Or choose "Surprise Me!" for random length

3. **Click "Invoke the Bard"**
   - Watch as your Shakespearean text generates
   - View statistics and performance metrics

4. **Copy & Share**
   - Use the copy button to grab the generated text
   - Share your AI-generated Shakespeare!

## 🛠️ Troubleshooting

### "Cannot connect to API server"
- Make sure the backend is running on port 8000
- Check that the backend URL in the code matches your setup

### CORS Errors
- The backend needs CORS enabled for the frontend to work
- Add this to your `main.py` (if not already there):
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

## 🎨 Customization

Feel free to customize the colors, fonts, or layout in the `<style>` section!

The current theme uses:
- Purple gradients (#667eea, #764ba2)
- Dark gray backgrounds (#2d3748, #1a202c)
- Georgia/Times New Roman serif fonts for that classical feel

## 📝 Notes

- The frontend is a single self-contained HTML file
- No build process required
- Works offline once loaded (API connection required for generation)
- Mobile-friendly and responsive

Enjoy creating Shakespearean gibberish! 🎭✨
