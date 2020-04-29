#!/usr/bin/python3
for i in range(-ord('z'), -(ord('a') - 1)):
    if (i % 2) != 0:
        i = i - (ord('A') - ord('a'))
    print("{}".format(chr(-i)), end='')
