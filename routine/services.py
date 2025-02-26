import requests

from config.settings import TELEGRAM_URL, TELEGRAM_BOT


def send_telegram_message(tg_chat_id, message):
    params = {
        'text': message,
        'chat_id': tg_chat_id,
    }

    requests.get(f'{TELEGRAM_URL}{TELEGRAM_BOT}/sendMessage', params=params)
