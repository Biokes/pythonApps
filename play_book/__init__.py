print("number square cube")
for number in range(5):
    print(f"{number: >6.0f} {number**2:>6.0f} {number**3:>4.0f}")
count =0
for number in range(10, 0,-1):
        print('*' * number)
for value in range(0,10):
    print(' '* value,end='' )
    for number in range(10-value,0,-1):
        print('*', end='')
    print()
for number in range(1,11):
    print(number*'*')