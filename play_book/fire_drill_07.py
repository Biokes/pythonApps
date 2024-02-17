def adjascentAsterisks():
    userInputs = []
    number = 1
    while number != 22:
        number = int(input("Enter a number and enter 22 to stop: "))
        while (number < 1 or number > 15) and number != 22:
            number = int(input("Enter a valid number or enter 22 to stop!!!!!: "))
        userInputs.append(number)
        if number == 22:
            break
    for count in userInputs:
        print(f"{count} :", end="")
        for num in range(count):
            print("*", end='')
        print()


print(adjascentAsterisks())
