import PySimpleGUI as sg

#sg.theme('Default1')
sg.theme('Light Brown 13')

layout = [[sg.Text('Rename files or folder')],
          [sg.T('Source Folders', size=(15, 5)), sg.In(), sg.FolderBrowse()],
          [sg.T('Source Files', size=(15, 1)), sg.In(), sg.FolderBrowse()],
          [sg.Submit(), sg.Cancel()]
          ]

window = sg.Window('Rename Files or Folders', layout)
event, values = window.read()
window.close()
print(event)
folder_path, file_path = values[0], values[1]
print(folder_path, file_path)
print(values)