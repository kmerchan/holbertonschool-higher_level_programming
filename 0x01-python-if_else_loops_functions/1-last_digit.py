#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end='')
if number >= 0:
    print("{} and is ".format(number % 10), end='')
    if (number % 10) > 5:
        print("greater than 5")
    elif (number % 10) == 0:
        print("0")
    else:
        print("less than 6 and not 0")
elif number < 0:
    number2 = 0 - number
    if (number2 % 10) == 0:
        print("{} and is 0". format(number2 % 10))
    else:
        print("-{} and is less than 6 and not 0". format(number2 % 10))
