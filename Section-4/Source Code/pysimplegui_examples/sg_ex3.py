import PySimpleGUI as sg

# name = sg.popup_get_text('Please enter your name')
# print(name)

# fs = sg.popup_get_file('Select File')
# print(fs)

# fs = sg.popup_get_file('Save file', save_as=True)
# print(fs)

folder = sg.popup_get_folder('Select Folder')
print(type(folder))
print(folder)