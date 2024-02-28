def is_on(name: str):
    if name[len(name) - 1] == '0':
        return True
    return False


def is_valid(number_given: str):
    for items in number_given:
        if items not in ('0', '1'):
            return False
    return True
