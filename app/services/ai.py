import requests
from config import HF_TOKEN
from app.data.prompts import PROMPTS

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_text(topic):
    prompt = PROMPTS[topic]

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 200,
                    "temperature": 0.7
                }
            },
            timeout=30
        )

        data = response.json()

        if isinstance(data, list):
            text = data[0]["generated_text"]
        else:
            return "❌ Ошибка генерации"

        # чистим prompt из ответа (HF часто возвращает его вместе)
        return text.replace(prompt, "").strip()

    except Exception as e:
        return "❌ Ошибка запроса к ИИ"

response = requests.post(
    API_URL,
    headers=headers,
    json={
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        }
    },
    timeout=30
)

print(response.json())  # 👈 ВАЖНО
