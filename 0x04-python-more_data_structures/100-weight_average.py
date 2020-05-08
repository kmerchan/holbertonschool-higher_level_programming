#!/usr/bin/python3
def weight_average(my_list=[]):
    count = 0
    summation = 0
    if my_list:
        for (x, y) in my_list:
            summation += (x * y)
            count += y
        average = summation / count
        return (average)
    else:
        return (0)
