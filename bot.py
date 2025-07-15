import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Asegúrate que en Render esté configurada la variable BOT_TOKEN correctamente
TOKEN = os.getenv("BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola Wilder, ¡bot activo en Render! 😎")

# Comando /saludo
async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Un saludo desde tu bot de Telegram!")

# Inicializar la aplicación
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("saludo", saludo))
    print("✅ Bot iniciado correctamente...")
    app.run_polling()

if __name__ == "__main__":
    main()
