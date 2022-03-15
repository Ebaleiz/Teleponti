from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import PySimpleGUI as sg

sg.theme('DarkGray')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Invia il tuo messaggio:')],
            [sg.Multiline(key='text', size=(50, 20), no_scrollbar=True)],
            [sg.Button('Invia'), sg.Button('Immagine')] ]


error = [ [sg.Text('ERRORE')] ]


# Create the Window
window = sg.Window('Teleponti', layout)


while True:
    event, values=window.read()
    testo=""
    if event=='Invia':
        for i in values['text']:
            testo=testo+i
        testo=testo.strip()
        if testo=="":
            sg.popup('ERRORE')
        else:
            print('You entered: ',testo)
    if event == sg.WIN_CLOSED:
        break
window.close()

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