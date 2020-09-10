import PySimpleGUI as sg

layout = [[sg.T(f'Input {i+1}'), sg.In(key=i)] for i in range(10)]
layout += [[sg.Save(), sg.Exit()]]

window = sg.Window('Example ', layout)
event, values = window.read()
window.close()