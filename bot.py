from telegram.ext import ApplicationBuilder, MessageHandler, filters
from chatbot import get_response

BOT_TOKEN = "7666255819:AAGSV0BXYWBvNxSZ0L6hLnIoD_TNweGyb8k"

async def handle_message(update, context):
    user_text = update.message.text
    reply = get_response(user_text)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
