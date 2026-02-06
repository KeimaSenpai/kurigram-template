from bot.client import app
from pyrogram import Client, filters
from pyrogram.types import Message

from bot.keyboards.inline import start_keyboard
from bot.language.languages import lang_manager
from bot.media.source import HOME_IMG

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    first_name = message.from_user.first_name
    lang_code = message.from_user.language_code
    bot_name = client.me.first_name


    # Si el kyc es false sale el boton con Inciar kyc si no sale el de perfil
    await message.reply_photo(
        HOME_IMG, 
        caption=lang_manager.get_text("welcome", lang_code).format(first_name=first_name, bot_name=bot_name) ,
        reply_markup= await start_keyboard()
    )