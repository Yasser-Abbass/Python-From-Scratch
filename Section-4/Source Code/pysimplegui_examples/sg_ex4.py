import PySimpleGUI as sg


for i in range(1000):
    flag = sg.one_line_progress_meter(title='My Progress meter',
                               current_value=i+1,
                               max_value=1000,
                               key='-PROGRESS-',
                               orientation='v')

    if not flag:
        break