import re


def count_alpha(alphabets: str):
    count = 0
    for letter in alphabets:
        if letter.isalpha():
            count += 1
    return count


def count_numbers(alphabets: str):
    count = 0
    for letter in alphabets:
        if letter.isnumeric():
            count += 1
    return count


def count_alpa_numerics(alphabets: str):
    return f"{"LETTERS"}  : {(len(list(filter(lambda given: given.isalpha(), alphabets))))}"


def count_characters(alphabets: str):
    counter = count_alpha(alphabets)
    count = count_numbers(alphabets)
    return f"letters = {counter}\nNumbers = {count}."


def count_UpperCases(alphabets: str):
    count = 0
    for letter in alphabets:
        if letter.isupper():
            count += 1
    return count


def count_lowerCases(alphabets: str):
    count = 0
    for letter in alphabets:
        if letter.islower():
            count += 1
    return count


def count_cases(alphabet: str):
    return_value = {"UPPER CASES": count_UpperCases(alphabet), "lower cases": count_lowerCases(alphabet)}
    return return_value


def count_upperAndLower_cases(alphabet: str):
    return {"UPPER CASES": len(list(filter(lambda given: given.isupper(), alphabet))),
            "lower cases": len(list(filter(lambda given: given.islower(), alphabet)))}


if __name__ == '__main__':
    print(count_characters("my name is 010 79"))
    print(count_cases("Hello world"))
    print(count_upperAndLower_cases("Hello world"))
    print(count_alpa_numerics("names"))
