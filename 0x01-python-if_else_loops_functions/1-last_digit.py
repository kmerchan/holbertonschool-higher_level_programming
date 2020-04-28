#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = 0 - number
else:
    number2 = number
print("Last digit of {} is {} and is ".format(number, (number2 % 10)), end='')
if (number2 % 10) > 5:
    print("greater than 5")
elif (number2 % 10) == 0:
    print("0")
else:
    print("less than 6 and not 0")
