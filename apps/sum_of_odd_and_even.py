number = int(input("Enter a number: "))
even = 0
odd = 0
for num in range(1, number):
    if num % 2 == 1:
        odd += num
    else:
        even += num
print(f"Sum of even numbers is {even}\nThe sum of odd is {odd}")
# lamda
# slicing