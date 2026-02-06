from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Canal", url="https://t.me/+m0MaiRddpmVlNWYx")
        ],
        [
            InlineKeyboardButton("Información", callback_data="info")
        ],
    ])
    


async def return_keyboard(callback="start"):
    """Teclado para volver al menú principal"""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Volver", callback_data=callback)
        ]
    ])