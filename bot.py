from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # Token tomado desde variables de entorno

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola Wilder! Tu bot ya está activo en Render 😎")

async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Saludos desde tu bot!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("saludo", saludo))
    print("✅ Bot iniciado correctamente...")
    app.run_polling()
