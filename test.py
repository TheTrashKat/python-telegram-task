
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text(f'Hello {update.effective_user.id}')


app = ApplicationBuilder().token("7151938763:AAGxmmdlLVKFN6rahNg9YneYjV_X5W5f8wc").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()