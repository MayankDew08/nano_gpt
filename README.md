# 🎭 Shakespeare's Digital Quill

**Where AI Meets the Bard's Eloquent Gibberish**

A beautiful web interface for your locally-trained NanoGPT model that generates Shakespearean text!

---

## 🚀 Quick Start

### Easiest Way - Double Click!
Simply double-click **`START.bat`** in this folder!

It will:
1. ✅ Start the backend API on port 8000
2. ✅ Start the frontend server on port 8080  
3. ✅ Open your browser automatically

### Manual Start

**Terminal 1 - Backend:**
```bash
cd Backend
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd Frontend
python -m http.server 8080
```

Then open: **http://localhost:8080**

---

## 🎯 What You Get

### Frontend Features
- 🎨 **Beautiful Theatrical UI** - Purple gradients and elegant Shakespeare theme
- 📝 **Optional Prompts** - Start with text or leave blank for randomness
- 🎲 **Smart Length Selection** - Pick exact tokens or random (500-2500)
- ⚡ **Live Performance Stats** - Generation time, tokens, and more
- 📋 **One-Click Copy** - Share your AI Shakespeare instantly
- 📱 **Fully Responsive** - Works on phones, tablets, and desktops

### Backend Features
- 🚀 **Fast API** - Optimized for quick responses
- 🧠 **Pre-trained Model** - Loads weights, no training overhead
- 📊 **Detailed Logging** - Response times logged to console
- 🎲 **Random Token Selection** - From [500, 750, 1000, 1500, 2000, 2500]
- 🔧 **Environment Config** - Easy customization via .env

---

## 📂 Project Structure

```
nano_gpt/
├── Backend/
│   ├── main.py              # FastAPI server with CORS
│   ├── model.py             # Clean GPT architecture (no training code)
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Configuration
│   ├── schemas/             # Pydantic models
│   └── services/            # Model loading service
├── Frontend/
│   ├── index.html           # Beautiful single-page app
│   └── README.md           # Frontend docs
├── model.pth               # Your trained model weights
├── input.txt               # Shakespeare training data
├── gpt.py                  # Original training script
└── START.bat               # Easy launcher!
```

---

## 🎨 Using the Interface

1. **Enter a Prompt** (or don't!)
   - Try: "To be or not to be"
   - Try: "Once upon a midnight"
   - Or leave blank for pure AI creativity

2. **Choose Generation Length**
   - Pick from 100 to 2000 tokens
   - Or select "Surprise Me!" for random

3. **Click "Invoke the Bard"**
   - Watch the magic happen
   - See real-time generation stats

4. **Copy & Share**
   - One-click clipboard copy
   - Share your AI Shakespeare!

---

## 🛠️ Technical Details

### Model Configuration
- **Architecture**: GPT (6 layers, 6 heads, 384 embedding dimensions)
- **Context Length**: 256 tokens
- **Training Data**: Shakespeare corpus
- **Vocabulary**: 65 unique characters

### API Endpoints
- `GET /` - API status and info
- `POST /generate` - Generate text
  - Body: `{"text": "optional prompt", "new_tokens": 1000}`
  - Returns: Generated text + stats

### Performance
- ⚡ Vocabulary loaded once at startup (zero overhead)
- ⚡ Encode/decode functions cached (instant)
- ⚡ Model loaded once (fast inference)
- ⚡ Response times logged for optimization

---

## 📝 Dependencies

Already in `Backend/requirements.txt`:
```
fastapi
uvicorn
torch
pydantic
python-dotenv
```

Install with:
```bash
cd Backend
pip install -r requirements.txt
```

---

## 🎭 Why "Shakespeare's Digital Quill"?

Your model was trained on Shakespeare's works, making it a perfect digital recreation of the Bard's writing style - complete with:
- Theatrical flourishes ✨
- Archaic language 📜
- Poetic rhythms 🎵
- Elizabethan charm 👑

...and yes, sometimes eloquent gibberish! 😄

---

## 🌟 Features Highlights

### What Makes This Special?
1. **Zero Training Overhead** - Loads pre-trained model only
2. **Beautiful UX** - Not just functional, but delightful
3. **Smart Caching** - Vocabulary loaded once, reused forever
4. **Performance Logging** - Every request timed and logged
5. **Random Length Magic** - Let the AI decide how much to write
6. **Single-File Frontend** - No build process, just open and use

---

## 🚨 Troubleshooting

### Backend won't start?
- Check if Python and dependencies are installed
- Make sure port 8000 is available
- Verify `model.pth` exists in nano_gpt folder

### Frontend shows CORS errors?
- CORS is now enabled in the backend
- Make sure backend started successfully

### Can't connect to API?
- Verify backend is running on http://localhost:8000
- Check backend terminal for errors
- Try visiting http://localhost:8000/docs

---

## 🎉 Have Fun!

You've built a complete AI text generation system from scratch:
- ✅ Trained your own model
- ✅ Built a professional API
- ✅ Created a beautiful interface

Now go forth and generate some Shakespearean magic! 🎭✨

---

*Made with 💜 and local AI*
