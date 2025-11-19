import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TOKEN = "8084336458:AAGxI1KDedLEhF7Lr6nksj_VMfbJpRhTvD0"  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
