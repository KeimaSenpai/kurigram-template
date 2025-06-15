from bot.client import app
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply("¡Hola! Soy tu bot de Telegram.")

@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = """
    📋 **Comandos disponibles:**
    
    /start - Iniciar el bot
    /help - Mostrar esta ayuda
    """
    await message.reply(help_text)