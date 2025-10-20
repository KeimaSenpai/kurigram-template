from bot.client import app
from bot.handlers import commands, callbacks

if __name__ == "__main__":
    print("Bot iniciado...")
    app.run()