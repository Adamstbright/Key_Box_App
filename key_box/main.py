import PySimpleGUI as sg
from functions import get_key_in_dict, new_file_content, append_new_key, get_key_in_list, delete_key

sg.theme("TealMono")

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
            if not user_input.startswith("230"):
                sg.popup("This is not Midas outlet ID")
            if user_input.isdigit():
                datas = get_key_in_dict()
                box = datas[user_input]
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
        datas = get_key_in_dict()
        outlet_to_add = value["ID_to_reg"]
        keybox_to_add = value["Keybox"].capitalize()
        if outlet_to_add in datas.keys():
            sg.popup("Outlet key already exist!")
        else:
            if len(outlet_to_add) > 8:
                sg.popup("Please enter valid outlet ID")
            elif len(outlet_to_add) < 7:
                sg.popup("Please enter valid outlet ID")
            elif len(keybox_to_add) != 1:
                sg.popup("Remember to input only keybox id e.g input C, for Box C")
            elif outlet_to_add.isdigit():
                details_to_add = [outlet_to_add, keybox_to_add]
                append_new_key(details_to_add)
                sg.popup("Out successfully added")
            else:
                sg.popup("Our outlets ID contains only digit")

    if event == "delete":
        datas = get_key_in_dict()
        outlet_to_delete = value['ID_to_reg']
        if outlet_to_delete not in datas.keys():
            sg.popup("Outlet does not Exist")
        elif len(outlet_to_delete) > 8:
            sg.popup("Please enter valid outlet ID")
        elif len(outlet_to_delete) < 7:
            sg.popup("Please enter valid outlet ID")
        else:
            data = get_key_in_list()
            new_data = delete_key(data, outlet_to_delete)
            new_file_content(new_data)
            sg.popup("Outlet successfully deleted!")

window.close()