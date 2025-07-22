import time
from telegram import Bot

TOKEN = "7962849790:AAFYEgvEErYBGavFoctuMpk-KhaTdiNdyKI"
CHAT_ID = "@asdfwt94"
LINK = "https://t.me/VARNEWS94"
DELAY = 1800

bot = Bot(token=TOKEN)
print("البوت يعمل الآن...")

while True:
    try:
        bot.send_message(chat_id=CHAT_ID, text=LINK)
        print(f"تم إرسال: {LINK}")
    except Exception as e:
        print(f"خطأ: {e}")
    time.sleep(DELAY)
