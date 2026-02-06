import os
from pathlib import Path

# Solo cargar .env si existe (desarrollo)
env_file = Path(".env")
if env_file.exists():
    from dotenv import load_dotenv
    load_dotenv()
    print("🔧 Modo desarrollo: variables cargadas desde .env")
else:
    print("🚀 Modo producción: usando variables de entorno del sistema")


API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMINS = [1618347551]  # IDs de administradores
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "BYTEBOT_DB")