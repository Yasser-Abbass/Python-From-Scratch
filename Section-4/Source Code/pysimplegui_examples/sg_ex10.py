import PySimpleGUI as sg


col = [[sg.Text('Col Row 1')]] + [[sg.T(f'Col Row {i+2}'), sg.In(f'col input {i+1}')] for i in range(10)]

layout = [[sg.Slider(range(1, 100), default_value=10, orientation='v', size=(8, 20)), sg.Column(col)],
          [sg.In('Last Input')],
          [sg.OK()]]

window = sg.Window('Column layout', layout)
event, values = window.read()

window.close()
sg.popup(event, values, line_width=200)