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
    set1.add(number)
    pass


def find_intersection(set1=set, set2=set) -> set:
    return set1 & set2


