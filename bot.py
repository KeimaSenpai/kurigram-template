import asyncio
from bot.client import app
from bot.handlers import commands, callbacks
import signal
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import suppress

shutdown_event = asyncio.Event()




def signal_handler(signum, frame):
    print(f"Señal {signum} recibida, iniciando cierre del bot")
    shutdown_event.set()

async def shutdown_handler():
    global current_task_should_stop
    current_task_should_stop = True
    print("Cerrando bot de forma segura...")
    await app.stop()
    print("Bot cerrado exitosamente")

# Configuración para la gestión de errores y desconexión
async def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    try:
        # Inicia el bot
        await app.start()
        # Optimizar conexión al datacenter más cercano
        # try:
        #     await app.set_dc()
        #     print("✅ Conexión optimizada al datacenter más cercano")
        # except Exception as e:
        #     print(f"⚠️ No se pudo optimizar datacenter: {e}")
        print('Bot iniciado')


        # await setup_commands(app)

        scheduler = AsyncIOScheduler()
        #scheduler.add_job(clean_cooldowns, 'interval', hours=1)
        scheduler.start()
        # Mantener el bot en ejecución hasta que se detenga
        try:
            await shutdown_event.wait()
        except:
            pass
        finally:
            await shutdown_handler()
            scheduler.shutdown()
    except Exception as e:
        print(f"Error en main: {e}")
        await shutdown_handler()

if __name__ == "__main__":
    # Configurar el bucle de eventos para ejecutar el bot de manera asíncrona
# uvloop.install()
# asyncio.run(main())
    loop = asyncio.get_event_loop()
    with suppress(KeyboardInterrupt):
        loop.run_until_complete(main())