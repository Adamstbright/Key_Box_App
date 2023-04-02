import csv
FILEPATH = "keys.csv"


def get_key_in_dict():
    with open(FILEPATH, "r") as file:
        content = csv.reader(file)
        datas = dict(content)
        return datas


def get_key_in_list():
    with open(FILEPATH, "r") as file:
        content = csv.reader(file)
        datas = list(content)
        return datas


def append_new_key(outlet_to_add):
    with open(FILEPATH, "a", newline='') as file:
        data = csv.writer(file)
        data.writerow(outlet_to_add)


def new_file_content(content):
    with open(FILEPATH, mode="w", newline="") as file:
        data = csv.writer(file)
        data.writerows(content)


def delete_key(content, outlet_to_delete):
    [content.remove(value) if value[0] == outlet_to_delete else exit for value in content]
    return content


if __name__ == "__main__":
    print(get_key_in_list())
    print(get_key_in_dict())