import PySimpleGUI as sg

# Define the layout of the window
layout = [
    [sg.Text("What's your name?")],
    [sg.InputText(key='-NAME-')],
    [sg.Text("Pick a number:")],
    [sg.Slider(range=(1, 10), orientation='h', key='-NUM-')],
    [sg.Button("Submit"), sg.Button("Exit")],
    [sg.Text("", key='-OUTPUT-', size=(30, 1))]
]

# Create the window
window = sg.Window("Simple Test App", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Submit':
        name = values['-NAME-']
        number = int(values['-NUM-'])
        greeting = f"Hello {name}, your number is {number}"
        window['-OUTPUT-'].update(greeting)

window.close()