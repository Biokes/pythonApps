from apps.class_examples.invalidnumbererror import InvalidNumberError


def is_on(name: str):
    if name[7] == '1':
        return True
    return False


def is_valid(number_given: str):
    if len(number_given) != 8 or not number_given.isnumeric():
        raise InvalidNumberError
    for items in number_given:
        if items not in ('0', '1'):
            raise InvalidNumberError
    return True


def get_shape_of_index_one_and_five(number: str):
    if is_valid(number):
        if number[1] == number[5] == "1":
            alphabet = "#"
            return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"
        if number[1] == number[5] == "0":
            alphabet = " "
            return f" {alphabet:>5}" + f"\n {alphabet:>5}"
        if number[1] == "1" and number[5] == "0":
            alphabet = "#"
            return f" {alphabet:>5}" + f"\n {alphabet:>5}"
        else:
            alphabet = " "
            return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"


def get_shape_of_index_two_and_four(number: str):
    if is_valid(number):
        if number[2] == number[4] == "1":
            alphabet = "#"
            return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"
        if number[2] == number[4] == "0":
            alphabet = " "
            return f" {alphabet:>5}" + f"\n {alphabet:>5}"
        if number[2] == "1" and number[4] == "0":
            alphabet = "#"
            return f" {alphabet:>5}" + f"\n {alphabet:>5}"
        else:
            alphabet = " "
            return f"#{alphabet:>5}" + f"\n#{alphabet:>5}"


def get_index_zero(number: str):
    if is_valid(number):
        if number[0] == "1":
            return f"{"#" * 6}"
        return f"{" "* 6}"


def get_index_three(number: str):
    if is_valid(number):
        if number[3] == "1":
            return f"{"#" * 6}"
        return f"{" ":>6}"


def get_index_seven(number: str):
    if is_valid(number):
        if number[6] == "1":
            return f"{"#" * 6}"
        return f"{" ":>6}"


def get_shape(number: str):
    if is_on(number):
        return (f"{get_index_zero(number)}\n{get_shape_of_index_one_and_five(number)}"
                f"\n{get_index_seven(number)}\n{get_shape_of_index_two_and_four(number)}" +
                f"\n{get_index_three(number)}")
    return "   "


print(get_shape("01100111"))
print(get_shape("00100111"))
print(get_shape("01100111"))
print(get_shape("11111111"))
print(get_shape("01100110"))
print(get_shape("01101111"))
