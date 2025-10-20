# 🤖 KuriGram Template

Una plantilla robusta y modular para crear bots de Telegram usando Python. Diseñada para ser fácilmente extensible y mantenible.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot_API-2CA5E0.svg)](https://core.telegram.org/bots/api)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Características

- ⚡ **Estructura Modular**: Organización clara y mantenible del código
- 🌐 **Soporte Multilenguaje**: Sistema integrado de traducción (es, en)
- 🎮 **Gestión de Comandos**: Sistema robusto de manejo de comandos
- ⌨️ **Teclados Dinámicos**: Soporte para teclados inline y reply
- 🎨 **Gestión de Medios**: Sistema integrado para manejar imágenes y recursos
- 🔄 **Reinicio Automático**: Sistema de reinicio programado
- 🐳 **Soporte Docker**: Despliegue simplificado con contenedores

## 📁 Estructura del Proyecto

```
bot/
├── config/         # Configuraciones y variables
├── handlers/       # Manejadores de eventos
├── keyboards/      # Definición de teclados
├── language/       # Sistema de traducciones
├── media/         # Recursos multimedia
├── plugins/       # Plugins extensibles
└── utils/         # Utilidades generales
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Token de bot de Telegram (@BotFather)

### Instalación

1. **Clonar el repositorio**
   ```powershell
   git clone https://github.com/KeimaSenpai/kurigram-template.git
   cd kurigram-template
   ```

2. **Crear y activar entorno virtual**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Instalar dependencias**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   
   Crea un archivo `.env` en la raíz del proyecto:
   ```env
   API_ID=tu_api_id
   API_HASH=tu_api_hash
   TELEGRAM_BOT_TOKEN=tu_token_bot
   ```

5. **Ejecutar el bot**
   ```powershell
   python bot.py
   ```

## 🛠️ Personalización

### Añadir Nuevos Comandos

1. Abre `bot/handlers/commands.py`
2. Añade tu nuevo comando siguiendo el patrón existente:

```python
@bot.on_message(filters.command("tucomando"))
async def cmd_tucomando(client, message):
    await message.reply("¡Tu respuesta aquí!")
```

### Crear Nuevos Teclados

1. En `bot/keyboards/inline.py` o `bot/keyboards/reply.py`
2. Define tu nuevo teclado:

```python
tu_teclado = InlineKeyboardMarkup([
    [InlineKeyboardButton("Botón 1", callback_data="btn1")]
])
```

### Añadir Nuevos Idiomas

1. Crea un nuevo archivo JSON en `bot/language/translations/`
2. Sigue el formato existente en los otros archivos de idioma

## 🐳 Despliegue con Docker

1. **Construir la imagen**
   ```powershell
   docker build -t kurigram-bot .
   ```

2. **Ejecutar el contenedor**
   ```powershell
   docker run --env-file .env kurigram-bot
   ```

## 📝 Buenas Prácticas

- ✅ Mantén los handlers pequeños y específicos
- ✅ Usa el sistema de traducciones para textos
- ✅ Documenta las funciones nuevas
- ✅ Sigue el estilo de código existente
- ❌ No subas tokens o archivos de sesión
- ❌ No modifiques directamente los archivos core

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de características
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- [@KeimaSenpai](https://github.com/KeimaSenpai) - *Desarrollador Principal*

## 🙏 Agradecimientos

- [Pyrogram](https://docs.pyrogram.org/) - Framework para Telegram
- [Python-Telegram-Bot](https://python-telegram-bot.org/) - Inspiración y referencia

