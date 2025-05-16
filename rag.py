import requests
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

# === Load environment variables ===
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "mistral-saba-24b"  # or llama3-70b-8192


def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    elif "youtube.com" in parsed_url.hostname:
        query = parse_qs(parsed_url.query)
        return query.get("v", [None])[0]
    return None


def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript_list])
    except Exception as e:
        print("❌ Error fetching transcript:", e)
        return None


def ask_question_groq(transcript, question):
    prompt = f"""You are a helpful assistant. Here's the transcript of a YouTube video:

Transcript:
{transcript}

Based only on this transcript, answer the question below.

Question: {question}
Answer:"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": GROQ_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 500
        }
    )

    if response.status_code != 200:
        print("❌ Groq API error:", response.text)
        return None

    return response.json()["choices"][0]["message"]["content"].strip()


def main():
    youtube_url = input("🔗 Enter YouTube video URL: ").strip()
    video_id = extract_video_id(youtube_url)

    if not video_id:
        print("❌ Invalid YouTube URL.")
        return

    print("⏳ Fetching transcript...")
    transcript = get_transcript(video_id)
    if not transcript:
        return

    print("✅ Transcript ready. Ask your questions below (type 'exit' to quit):\n")

    while True:
        question = input("❓ Your question: ").strip()
        if question.lower() in ["exit", "quit"]:
            break

        answer = ask_question_groq(transcript, question)
        print(f"\n💬 Answer: {answer}\n")


if __name__ == "__main__":
    main()
