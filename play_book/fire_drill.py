def input_seperator(number):
    list1 = {}
    count = 0
    for num in number:
        appearance = number.count(num)
        if num  not in list1:
            list1.keys( {num: appearance})
            # assume dictionary name is numbers
            # numbers = {key: value, key_one: value_two}
            # numbers[key] = new_value # when you want to change the value of a key

        else:
            continue

    return list1


sample = 'google.com'
print(input_seperator(sample))
