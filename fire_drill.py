list1 = []
def fill_list(list1):
    for num in range(10):
        number_collected = int(input("Enter  number btw 10 and 50: "))
        list1.append(number_collected)
        return list1
def get_length(list1):
        length = 0
        for elements in list1:
            length += 1
        return length
def index_in_even_positions_sum_up(listGiven):
    sum_up = 0
    for elements in range(len(listGiven)):
        if elements % 2 == 1:
            sum_up += listGiven[elements]
    return sum_up
def index_in_odd_positions_sum_up(listGiven):
    sum_up = 0
    for elements in range(len(listGiven)):
        if elements % 2 == 0:
            sum_up += listGiven[elements]
    return sum_up
def index_in_third_positions_sum_up(listGiven):
    sum_up = 0
    for elements in range(0, len(listGiven), 3):
            sum_up += listGiven[elements]
    return sum_up
def index_in_third_positions_multiplication(listGiven):
    sum_up = 1
    for elements in range(0, len(listGiven), 3):
        sum_up *= listGiven[elements]
    return sum_up
def average(listGiven):
    sum_up = 0
    for elements in range(len(listGiven)):
            sum_up+= listGiven[elements]
    return sum_up/(len(listGiven))
def get_largest_elements(list_variable):
        largest = list_variable[0]
        for numbers in range(len(list_variable)):
            if largest < list_variable[numbers]:
                largest = list_variable[numbers]
        return largest


def get_smallest_elements(list_variable):
    smallest = list_variable[0]
    for numbers in range(len(list_variable)):
        if list_variable[numbers] <  smallest:
            smallest = list_variable[numbers]
    return smallest
