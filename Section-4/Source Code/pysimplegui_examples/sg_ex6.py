import PySimpleGUI as sg


layout = [[sg.T('Files Dialog')],
          [sg.In(key='-IN-'), sg.FileBrowse(target='-IN-', file_types=(("Text Files", "*.txt"),('Docuemts', '*.docx'),))],
          [sg.OK(), sg.Exit()]
          ]

window = sg.Window('File Browse', layout)
event, values = window.read()
print(event)
print(values)
print(values['-IN-'])