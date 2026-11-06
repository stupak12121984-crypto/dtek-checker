import os
import requests

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

def check_schedule():
    message = "<b>График ДТЭК (Одесса):</b>\nСкрипт проверки запущен и работает!"
    send_telegram(message)

if __name__ == "__main__":
    check_schedule()
  
