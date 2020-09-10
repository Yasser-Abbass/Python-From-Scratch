import PySimpleGUI as sg


layout = [[sg.Text('Enter something'), sg.In(key='-IN-')],
          [sg.T('Output will go here', key='-OUT-')],
          [sg.OK(), sg.Cancel()]
          ]

window = sg.Window('Title', layout)
while True:
    event, values = window.read()
    window['-OUT-'].update(values['-IN-'])
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break

print(event)
print(values)
