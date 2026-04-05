import requests
import time
from config import HF_TOKEN
from app.data.prompts import PROMPTS

API_URL = "https://router.huggingface.co/api/models/mistralai/Mistral-7B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_text(topic):
    prompt = PROMPTS[topic]

    for _ in range(3):  # retry
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
            print("HF RESPONSE:", data)  # 👈 лог

            # ✅ если норм ответ
            if isinstance(data, list):
                text = data[0]["generated_text"]
                return text.replace(prompt, "").strip()

            # ❌ если модель грузится
            if "loading" in str(data).lower():
                time.sleep(5)
                continue

            # ❌ другая ошибка
            return f"❌ HF ошибка: {data}"

        except Exception as e:
            return f"❌ Ошибка запроса: {e}"

    return "❌ Модель не загрузилась"
