from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5110232242:AAFcZLSungEdAm-VPMnkt5WkYtsq5JN9ccI')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

def sent_messages(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("start")
    print("start called from chat with id = {}".format(chat_id))

updater.start_polling()
updater.idle()
