def enumerate_list(list):
    # para no modificar la lista, creamos una nueva
    enumerated_list = []
    for index, color in enumerate(list):
        if list[index] == "":
            del list[index]
            enumerated_list.append(f'{index}. {list[index]}')
            list.insert(index, color)
        else:
            enumerated_list.append(f'{index}. {color}')
    return enumerated_list


def enumerate_backwards(other_list):
    enumerated_list_backwards = []
    for index, color in enumerate(other_list):
        if other_list[index] == "":
            del other_list[index]
            enumerated_list_backwards.append(f'{index}. {other_list[index][::-1]}')
            other_list.insert(index, color)
        else:
            enumerated_list_backwards.append(f'{index}. {color[::-1]}')
    return enumerated_list_backwards
