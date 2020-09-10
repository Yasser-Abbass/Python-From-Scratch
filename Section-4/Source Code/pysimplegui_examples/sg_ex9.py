import PySimpleGUI as sg


def todoitem(num):
    return [sg.T(f'{num}. '), sg.CBox(''), sg.In()]


layout = [todoitem(i) for i in range(1, 10)] + [[sg.Save(), sg.Exit()]]
window = sg.Window('To Do List', layout)
event, values = window.read()