def input_collector():
    list1 = []
    for number in range(10):
        user_input = int(input("enter a number: "))
        if user_input not in list1:
            list1.append(user_input)
    return list1


def sum_collector(set1):
    total = 0
    for element in range(len(set1)):
        total += set1[element]
    return total


def remove_elements(number, set1):
    if number in set1:
        set1.remove(number)
        return number
    set1.append(number)
    return set1


# def find_intersection(set1=set, set2=set) -> set:
#     return set1 & set2


def list_creator():
    list1 = []
    for num in range(1, 16):
        list1.append(num)
    return list1


def duplicate_creator(list1):
    output_list = []
    for number in list1:
        output_list.append(number)
        output_list.append(number)
    return output_list


def eliminate_duplicates(list1):
    output_list = []
    for numbers in list1:
        if numbers not in output_list:
            output_list.append(numbers)
    return output_list


def add_Third_elements(list1):
    output_list = []
    for elements in range(1, len(list1)):
        if elements % 3 == 0:
            output_list.append(list1[elements - 1])
    return output_list


def get_sum(list1):
    output = 0
    if len(list1) % 2 == 0:
        length = len(list1)
        output = list1[0] + ((list1[(length // 2)-1] + list1[length // 2]) / 2) + list1[length - 1]
    else:
        length = (len(list1))
        output = list1[0] + list1[(length // 2)] + list1[length - 1]
    return output


def intersect_two_list(param, param1):
    for numbers in param1:
        if numbers in param:
            continue
        else:
            param1.remove(numbers)
    if param1:
         return param1
    else:
        return "No intersection between list"

