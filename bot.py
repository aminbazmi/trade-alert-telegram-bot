import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ پیام با موفقیت ارسال شد.")
    else:
        print("❌ ارسال پیام ناموفق بود:", response.text)

# تست اولیه
if __name__ == "__main__":
    send_alert("امین جان! این یه پیام تستی از بات خودته 😎🚀")
