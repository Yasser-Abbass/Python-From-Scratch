from backup import backup
from pathlib import Path
import PySimpleGUI as sg
sg.theme('DEFAULT1')

col = [[sg.CB('Compress', key='-COMP-')],
       [sg.CB('Recursive', key='-REC-')],
       [sg.T('Extension'), sg.I(key='-EXT-', size=(8, 1), default_text='*.*')]
       ]
layout = [[sg.T('Choose a source folder', size=(20, 1)), sg.In(key='-SRC-', enable_events=True),
           sg.FolderBrowse(target='-SRC-', tooltip='Select Source folder')],
          [sg.T('Choose a destination folder', size=(20, 1)), sg.In(key='-DEST-', enable_events=True),
           sg.FolderBrowse(target='-DEST-', tooltip='Select Destination folder')],
          [sg.T('File list')],
          [sg.Multiline(size=(45, 20), key='-FILES-'), sg.Col(col)],
          [sg.B('Backup', key='Backup'), sg.Exit()]
          ]

window = sg.Window('Backup', layout)
while True:
    event, values = window.read()
    if event == '-SRC-':
        src = Path(values['-SRC-'])
        ext = values['-EXT-']
        files = src.rglob(ext)
        files = list(files)
        window['-FILES-'].update(value='')
        #window['-FILES-'].Widget.config(wrap='none')
        if files:
            chrs = max([len(str(x)) for x in files])
            for fs in files:
                window['-FILES-'].print(fs)
            window['-FILES-'].set_size(size=(chrs, None))
    elif event == '-DEST-':
        dest = Path(values['-DEST-'])
        empty = next(dest.iterdir(), None)
        if empty:
            btn = sg.popup_ok_cancel('Destination contains files, if you proceed it will be deleted?')
            if btn == 'Cancel':
                window['-DEST-'].update(value="")
    elif event == 'Backup':
        src = Path(values['-SRC-'])
        dest = Path(values['-DEST-'])
        comp = values['-COMP-']
        rec = values['-REC-']
        ext = values['-EXT-']
        backup(src, dest, rec, comp, ext)
        sg.popup('Operation completed successfully')
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
