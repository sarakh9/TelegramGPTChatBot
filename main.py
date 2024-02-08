from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes, MessageHandler
TOKEN: Final = '6858031921:AAFgvORI9jFcYWT8j1vBvpot5seYE5hOfJk'
BOT_USERNAME :Final = '@gptchatbotbotbot'

# Commands

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hi!
                                    I am CatBot!
                                    If you need /help hit help command.
                                    """)

async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hi!
                                    I am CatBot!
                                    If you need /help hit help command.
                                    """)

async def costumCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hi!
                                    I need to be costumised!
                                    """)

# Response Handler

def handleResponse(text: str) -> str:
    return "I'm not working yet! I'm under develope."

# Message Handler

async def handleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type = update.message.chat.type
    text = update.message.text
    user = update.message.chat.id
    response = handleResponse(text)
    await update.message.reply_text(response)

# Error Handler

async def handleError(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == "__main__":
    print("Starting Bot...")
    app = Application.builder().token(TOKEN).build()

    #Commands

    app.add_handler(CommandHandler('start', startCommand))
    app.add_handler(CommandHandler('help', helpCommand))
    app.add_handler(CommandHandler('costum', costumCommand))

    # Message

    app.add_handler(MessageHandler(filters.TEXT, handleMessage))

    # Error

    app.add_error_handler(handleError)

    # Polling
    print("Polling...")
    app.run_polling(poll_interval=3)
