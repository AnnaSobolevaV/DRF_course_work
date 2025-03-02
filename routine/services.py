import requests

from config.settings import TELEGRAM_URL, TELEGRAM_BOT


def send_telegram_message(tg_chat_id, message):
    """Функция, отправляющая по tg_chat_id сообщение message по TELEGRAM_URL в TELEGRAM_BOT"""
    params = {
        'text': message,
        'chat_id': tg_chat_id,
    }

    requests.get(f'{TELEGRAM_URL}{TELEGRAM_BOT}/sendMessage', params=params)
