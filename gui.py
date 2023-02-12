import PySimpleGUI as sg
import pygame
from compare import classifier
myfont=("Helvetica", 14)
output=sg.Text(font=myfont)

sg.theme('DarkAmber')   
pygame.mixer.init()
layout = [  [sg.Text('Enter the nepali song that you want to find genre of',font=myfont)],
            [sg.Text('song name',font=myfont), sg.InputText(), sg.FileBrowse()],
            [sg.Text('Music Player', size=(30, 1), font=myfont)],
            [sg.Button('Play', size=(10, 2), font=myfont), sg.Button('Stop', size=(10, 2), font=myfont)],
            [sg.Text(size=(50, 1), font=myfont, key='status')],
            [output]]

window = sg.Window('music genre classification system', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event == 'Play':
        try:
            pygame.mixer.music.load(values[0])
            pygame.mixer.music.play()
            window['status'].update('Now playing: ' + values[0])
        except:
            window['status'].update('Please select a file to play')
    elif event == 'Stop':
        pygame.mixer.music.stop()
        window['status'].update('')
    if event == sg.WIN_CLOSED:
        break
    genre=classifier(values[0])
    output.update(genre)
    

window.close()
pygame.mixer.quit()
