
# 📘 YouTube Q&A Bot using Groq API

This is a command-line Python bot that:
- Takes a **YouTube video URL**  
- Automatically fetches its **transcript**
- Uses the **Groq LLM API** to answer questions based only on the transcript

No Flask. No frontend. Just a simple and fast CLI bot.

---

## ⚙️ Features

- 🔗 Paste any YouTube URL (with available captions)
- 📄 Fetches transcript automatically
- 💡 Ask natural language questions
- ⚡ Answers powered by **Groq's Mixtral or LLaMA3** models
- 🔐 API key is securely loaded via `.env` file

---

## 📦 Requirements

```bash
pip install youtube-transcript-api requests python-dotenv
```

---

## 📁 Project Structure

```
.
├── yt_qabot_groq.py     # Main script
├── .env                 # Your Groq API key (not shared)
└── README.md            # This file
```

---

## 🔐 Setup

1. **Get your Groq API key:**  
   https://console.groq.com/keys

2. **Create `.env` file:**

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ How to Run

```bash
python yt_qabot_groq.py
```

Example flow:

```bash
🔗 Enter YouTube video URL: https://www.youtube.com/watch?v=Ilg3gGewQ5U
⏳ Fetching transcript...
✅ Transcript ready. Ask your questions below (type 'exit' to quit):

❓ Your question: What is the main idea of the video?

💬 Answer: [response from Groq LLM]
```

---

## 🧠 Models Supported

Update the `GROQ_MODEL` variable in the script to:

- `mixtral-8x7b-32768` (default)
- `llama3-70b-8192`
- `gemma-7b-it`
- `mistral-saba-24b`

---

## 🚫 Limitations

- Only works with videos that have transcriptions available (no auto-captions in some cases).
- Transcript is limited to the maximum token length of the model (around 30k tokens for Mixtral).
- No offline support or local LLMs.

---

## ✅ Future Improvements (Optional)

- Stream LLM responses token-by-token
- Cache transcripts for reuse
- Add transcript summarization
- Add CLI args for automation

---

## 📜 License

MIT License — use freely, modify openly. Attribution appreciated.
