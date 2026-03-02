import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Define your token here
TOKEN = '7940204027:AAH3lTgEM_VGlkqYfq-tyROVL0QcEyg_Ol0'

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Subscribe Now", callback_data='subscribe')],
        [InlineKeyboardButton("Contact Support", url='https://t.me/ParadiseSupport')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome to Paradise Crypto VIP Bot! Choose an option:', reply_markup=reply_markup)

# Callback for buttons
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'subscribe':
        await query.edit_message_text("You have subscribed successfully!")

# Main function with proper shutdown handling
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Adding handlers for commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    # Running the bot with proper async handling
    try:
        await app.run_polling()
    finally:
        await app.shutdown()

# Run the bot using asyncio.run to avoid event loop issues
if __name__ == '__main__':
    asyncio.run(main())  # Correctly running the event loop
