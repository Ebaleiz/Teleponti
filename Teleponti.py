import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import PySimpleGUI as sg

sg.theme('DarkGray')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Invia il tuo messaggio:')],
            [sg.Multiline(key='text', size=(50, 20), no_scrollbar=True)],
            [sg.Button('Invia'), sg.Input(key='File', visible=False, enable_events=True), sg.FileBrowse('Immagine')] ]


error = [ [sg.Text('ERRORE')] ]


# Create the Window
window = sg.Window('Teleponti', layout, icon='icona.ico')

TELEGRAM_BOT_TOKEN = 'TOKEN'
TELEGRAM_CHAT_ID = '-769014460'

def start(update: Update, context: CallbackContext) -> None:
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    while True:
        event,values=window.read()
        testo=""
        img=""
        if event=='Invia':
            for i in values['text']:
                testo=testo+i
            testo=testo.strip()
            if testo=="":
                sg.popup('ERRORE: Nessun Messaggio inserito', icon='icona.ico')
            else:
                try:
                    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=testo)
                except:
                    sg.popup('ERRORE: Problema di rete', icon='icona.ico')
        if event == 'File':
            for y in values['File']:
                img=img+y
            img_test=img[-3:]
            if img_test=='':
                sg.popup('ERRORE: Nessuna immagine inserita', icon='icona.ico')
            elif img_test!='png':
                sg.popup('ERRORE: Solo PNG', icon='icona.ico')
            else:
                try:
                    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(img, 'rb'))
                except:
                    sg.popup('ERRORE: Problema di rete', icon='icona.ico')
        if event == sg.WIN_CLOSED:
            break
    window.close()
    


updater = Updater('5110232242:AAFcZLSungEdAm-VPMnkt5WkYtsq5JN9ccI')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
