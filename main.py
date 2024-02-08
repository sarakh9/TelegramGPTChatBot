from typing import Final
from telegram import Update
from telegram.ext import Applications, CommandHandler, filters, ContextTypes
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

async def costumeCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hi!
                                    I need to be costumised!
                                    """)
