import requests
from config import GROQ_API_KEY
from app.data.prompts import PROMPTS

API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


def generate_text(topic):
    print("KEY:", GROQ_API_KEY)
    prompt = PROMPTS[topic]

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            },
            timeout=30
        )

        data = response.json()
        print("GROQ RESPONSE:", data)  # лог для дебага

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Ошибка генерации: {e}"
        print("Не удалось получить текст")
