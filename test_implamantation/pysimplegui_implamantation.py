import PySimpleGUI as sg
import pandas as pd

def check_roles(file_a, file_b):
    df_a = pd.read_excel(file_a)
    df_b = pd.read_excel(file_b)

    # Normalize emails
    df_a['Email'] = df_a['Email'].str.strip().str.lower()
    df_b['Email'] = df_b['Email'].str.strip().str.lower()

    # Merge data
    merged = df_a.merge(df_b, on='Email', how='left')

    def get_expected(row):
        roles = []
        if str(row.get('Engineer', '')).lower() == 'yes':
            roles.append('Engineer')
        if str(row.get('Mathematician', '')).lower() == 'yes':
            roles.append('Mathematician')
        if str(row.get('In group?', '')).lower() == 'yes':
            group = str(row.get('Group', ''))
            if group and group.upper() != 'N/A':
                roles.append(group)
        return ', '.join(roles)

    merged['Expected'] = merged.apply(get_expected, axis=1)
    merged['Status'] = merged.apply(lambda r: "✅ OK" if r['Roles'].strip() == r['Expected'].strip() else "❌ Mismatch", axis=1)

    return merged[merged['Status'] == '❌ Mismatch'][['Email', 'Roles', 'Expected', 'Status']]

# GUI layout
layout = [
    [sg.Text("File A (with Roles):"), sg.Input(key='-FILEA-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text("File B (source file):"), sg.Input(key='-FILEB-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Button("Check"), sg.Button("Exit")],
    [sg.Text("Mismatches:")],
    [sg.Multiline(size=(100, 20), key='-OUTPUT-')]
]

window = sg.Window("Roles Validator", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Check':
        try:
            mismatches = check_roles(values['-FILEA-'], values['-FILEB-'])
            if mismatches.empty:
                window['-OUTPUT-'].update("✅ All rows match!")
            else:
                window['-OUTPUT-'].update(mismatches.to_string(index=False))
        except Exception as e:
            window['-OUTPUT-'].update(f"❌ Error: {e}")

window.close()