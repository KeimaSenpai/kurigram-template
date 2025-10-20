from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Canal", url="https://t.me/+m0MaiRddpmVlNWYx")
        ],
        [
            InlineKeyboardButton("Información", callback_data="info")
        ],
    ])
    


def return_keyboard():
    """Teclado para volver al menú principal"""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Volver", callback_data="start")
        ]
    ])