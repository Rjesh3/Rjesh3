from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Snake Game Bot! Click the link below to play:\n"
        "[Play Snake](https://playsnake.org/)",  # Example link
        parse_mode="Markdown"
    )

# Main function to run the bot
def main():
    # Replace with your Telegram Bot token
    BOT_TOKEN = "7670217902:AAGkDv4hj2Sl_DfuUOdyV0lRJTg4UXdfq70"

    app = ApplicationBuilder().token('7670217902:AAGkDv4hj2Sl_DfuUOdyV0lRJTg4UXdfq70').build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


    main()