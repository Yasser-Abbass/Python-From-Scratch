import PySimpleGUI as sg


menu = [['&File', ['&New', '&Open', '&Save', '---', 'E&xit']],
        ['&Edit', ['Copy', ['One', 'Two']], 'Paste']
        ]

layout = [[sg.Menu(menu)],
          [sg.Multiline(size=(30, 30), key='-TXT-')],
          [sg.OK(), sg.Exit()]
          ]

window = sg.Window('Menu Test', layout)
event, values = window.read()
window.close()
print(event)
print(values)