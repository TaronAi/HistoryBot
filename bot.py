import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Read token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello")

def main():
    # If the token is missing, show a clear error
    if not TOKEN:
        raise ValueError(
            "Error: TELEGRAM_BOT_TOKEN environment variable is not set.\n"
            "Set it before running the bot."
        )

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
