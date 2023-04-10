import csv
FILEPATH = "keys.csv"


def get_key_in_dict():
    """ This function read the CSV file and
    return a dictionary that contain shop ID
    as keys and keybox as values
    """
    with open(FILEPATH, "r") as file:
        content = csv.reader(file)
        datas = dict(content)
        return datas


def get_key_in_list():
    """ This function read the CSV file and
    return a list of lists
    """
    with open(FILEPATH, "r") as file:
        content = csv.reader(file)
        datas = list(content)
        return datas


def append_new_key(outlet_to_add):
    """ This function appends new list into
    a new line in the filepath
    """
    with open(FILEPATH, "a", newline='') as file:
        data = csv.writer(file)
        data.writerow(outlet_to_add)


def new_file_content(content):
    """ This function write updated data back
    into the filepath.
    """
    with open(FILEPATH, mode="w", newline="") as file:
        data = csv.writer(file)
        data.writerows(content)


def delete_key(content, outlet_to_delete):
    """ This function take 2 arguments and delete second
    argument from a list (the first argument)
    """
    for value in content:
        if value[0] == outlet_to_delete:
            content.remove(value)
        else:
            pass
    return content



if __name__ == "__main__":
    print(get_key_in_list)
    print(get_key_in_dict())


