def enumerate_list(list):
    # para no modificar la lista, creamos una nueva
    enumerated_list = []
    for index, color in enumerate(list):
        if list[index] != "":
            enumerated_list.append(f'{len(enumerated_list)}. {color}')
    return enumerated_list


def enumerate_backwards(other_list):
    enumerated_list_backwards = []
    for index, color in enumerate(other_list):
        if other_list[index] != "":
            enumerated_list_backwards.append(f'{len(enumerated_list_backwards)}. {color[::-1]}')
    return enumerated_list_backwards
