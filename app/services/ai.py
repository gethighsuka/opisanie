import requests
import time
from config import HF_TOKEN
from app.data.prompts import PROMPTS

# Новый URL Hugging Face Router
API_URL = "https://router.huggingface.co/api/models/mistralai/Mistral-7B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_text(topic, max_tokens=200):
    """
    Генерация текста (например, хештегов) по теме.
    Возвращает строку ответа модели или None при ошибке.
    """
    if topic not in PROMPTS:
        print(f"[ERROR] Тема '{topic}' не найдена в PROMPTS")
        return None

    prompt = PROMPTS[topic]
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_tokens}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # выброс ошибки при HTTP-коде != 2xx

        # Выводим JSON для дебага
        data = response.json()
        print("[DEBUG] Response JSON:", data)

        # Проверяем структуру ответа
        if isinstance(data, dict) and "error" in data:
            print("[ERROR] Hugging Face error:", data["error"])
            return None
        elif isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            print("[WARN] Неожиданный формат ответа:", data)
            return None

    except requests.exceptions.HTTPError as e:
        print("[HTTP ERROR]", e, response.text)
    except requests.exceptions.RequestException as e:
        print("[REQUEST ERROR]", e)
    except Exception as e:
        print("[OTHER ERROR]", e)

    return None

# Пример использования
if __name__ == "__main__":
    topic = "hashtags"
    result = generate_text(topic)
    if result:
        print("Generated text:", result)
    else:
        print("Не удалось получить текст")
