import PySimpleGUI as sg
from compare import classifier
myfont=('Roboto Mono',13)
output=sg.Text(font=myfont)

sg.theme('DarkAmber')   

layout = [  [sg.Text('Enter the nepali song that you want to find genre of',font=myfont)],
            [sg.Text('song name',font=myfont), sg.InputText(), sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [output]]


window = sg.Window('music genre classification system', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    genre=classifier(values[0])
    output.update(genre)

window.close()