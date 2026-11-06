import os
import requests

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_telegram(text):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Ошибка: TELEGRAM_TOKEN или CHAT_ID не найдены в Secrets!")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Статус отправки в Telegram: {response.status_code}")
        print(f"Ответ Telegram: {response.text}")
    except Exception as e:
        print(f"Ошибка при запросе к Telegram API: {e}")

def check_schedule():
    print("Запуск проверки графика...")
    message = "<b>График ДТЭК (Одесса, Группа 1.2):</b>\nТестовая проверка связи прошла успешно! ⚡"
    send_telegram(message)

if __name__ == "__main__":
    check_schedule()
    
