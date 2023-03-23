import PySimpleGUI as sg

sg.popup("Welcome to Midas Keybox App", text_color="Blue", background_color="white")

id_label1 = sg.Text("Outlet ID")
input1 = sg.Input(key="outlet id")
check_button = sg.Button("Check", key="check")
id_label2 = sg.Text("Register new key here")
register_button = sg.Button("Register", key="Register")
exit_Button = sg.Button("Exit", key="Exit")

layout1 = [[id_label1, input1], [check_button], [exit_Button, id_label2, register_button]]

id_label3 = sg.Text("Outlet ID")
input2 = sg.Input(key="ID_to_reg", tooltip="Input the outlet ID here!")
id_label4 = sg.Text("Key Box", tooltip="Enter Keybox where you kept the key")
input3 = sg.Input(key="Keybox")
add_button = sg.Button("Add Key", key="add")
delete_button = sg.Button("Delete Key", key="delete")
back_button = sg.Button("Back", key="back")

layout2 = [[id_label3, input2, add_button], [id_label4, input3, delete_button], [back_button]]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]

window = sg.Window("Midas Keybox App", layout)

datas = {"2300115": "A", "2300123": "B", "2300998": "C", "2300114": "K"}

layout = 1
while True:
    event, value = window.read()
    print(event, value)
    print(type(event))

    if event in (None, 'Exit'):
        break

    if event == "check":
        try:
            user_input = value["outlet id"]
            if user_input.isdigit():
                box = datas[a]
                sg.popup(f"The key is in Box {box}.")
            else:
                sg.popup("Our outlets ID contains only digit")
        except KeyError:
            sg.popup("Outlet Key not present in Keybox.")

    if event == "Register":
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 2 else 1
        window[f'-COL{layout}-'].update(visible=True)

    elif event == "back":
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 2 else 1
        window[f'-COL{layout}-'].update(visible=True)

    if event == "add":
        outlet_to_add = value["ID_to_reg"]
        keybox_to_add = value["Keybox"].capitalize()
        if len(outlet_to_add) > 8:
            sg.popup("Please enter valid outlet ID")
        elif len(outlet_to_add) < 7:
            sg.popup("Please enter valid outlet ID")
        elif len(keybox_to_add) != 1:
            sg.popup("Remember to input only keybox id e.g input C, for Box C")
        elif outlet_to_add.isdigit():
            datas[outlet_to_add] = keybox_to_add
            print(datas)
        else:
            sg.popup("Our outlets ID contains only digit")



    if event == "delete":
        outlet_to_delete = value['ID_to_reg']
        if outlet_to_delete not in datas.keys():
            sg.popup("Outlet does not Exist")
        elif len(outlet_to_delete) > 8:
            sg.popup("Please enter valid outlet ID")
        elif len(outlet_to_delete) < 7:
            sg.popup("Please enter valid outlet ID")
        else:
            del datas[outlet_to_delete]

window.close()
