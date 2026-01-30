import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from chatbot import get_response

TOKEN = os.environ.get("7666255819:AAGSV0BXYWBvNxSZ0L6hLnIoD_TNweGyb8k")

async def reply(update, context):
    text = update.message.text
    response = get_response(text)
    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot running on Railway...")
app.run_polling()
