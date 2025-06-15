from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("info"))
async def info_command(client: Client, message: Message):
    """Información del usuario"""
    user = message.from_user
    info_text = f"""
👤 **Tu información:**

🆔 **ID:** `{user.id}`
👤 **Nombre:** {user.first_name}
📱 **Usuario:** @{user.username if user.username else 'Sin username'}
🔤 **Idioma:** {user.language_code if user.language_code else 'No especificado'}
🤖 **Es bot:** {'Sí' if user.is_bot else 'No'}
    """
    await message.reply(info_text)