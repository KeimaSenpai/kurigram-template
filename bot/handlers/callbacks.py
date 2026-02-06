from pyrogram.types import Message, CallbackQuery
from bot.client import app
from pyrogram import Client, filters

from bot.keyboards.inline import start_keyboard, return_keyboard
from bot.language.languages import lang_manager

@app.on_callback_query(filters.regex("^start$"))
async def start_callback(client, callback_query):
    # Obetemos el nombre del usuario
    first_name = callback_query.from_user.first_name
    lang_code = callback_query.from_user.language_code
    bot_name = client.me.first_name
    # Editamos el mensaje de bienvenida
    await callback_query.edit_message_text(
        lang_manager.get_text("welcome", lang_code).format(first_name=first_name, bot_name=bot_name),
        reply_markup= await start_keyboard()
    )


@app.on_callback_query(filters.regex("^info$"))
async def info_callback(client: Client, callback_query: CallbackQuery):
    lang_code = callback_query.from_user.language_code
    # Editamos el mensaje de información
    await callback_query.edit_message_text(
        lang_manager.get_text("info", lang_code),
        reply_markup= await return_keyboard()
    )