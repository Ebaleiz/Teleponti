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
