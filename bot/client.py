from pyrogram import Client, filters, types
from bot.config.var import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "mi_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot/plugins")
)

# Diccionario para almacenar datos de usuarios temporalmente
app.user_data = {}


@app.on_pre_checkout_query()
async def pre_checkout_query_handler(_: Client, query: types.PreCheckoutQuery):
    await query.answer(ok=True)

@app.on_message(filters.successful_payment)
async def successful_payment_handler(client: Client, message: types.Message):
    """Procesar el pago exitoso"""

    try:
        # Obtener datos del pago
        payment_info = message.successful_payment
        # payload = payment_info.invoice_payload
        # user_id = message.from_user.id

        
        await message.reply_text(
            f"✅ Pago recibido con éxito!\n\n Monto: {payment_info.total_amount / 100} {payment_info.currency}\n"
        )
            
    except Exception as e:
        print(f"Error procesando pago: {e}")
        await message.reply_text(
            "❌ Ocurrió un error al procesar el pago. Por favor, contacta al soporte."
        )