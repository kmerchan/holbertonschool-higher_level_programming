#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print("0", end='')
    print("{}, ".format(i), end='')
print("99")
