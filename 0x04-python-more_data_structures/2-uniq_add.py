#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    new_list = sorted(my_list)
    for i in range(len(new_list)):
        if i == 0 or new_list[i] != new_list[i - 1]:
            summation += new_list[i]
    return(summation)
