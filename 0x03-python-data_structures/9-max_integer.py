#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        new_list = [my_list[0]]
        for i in my_list:
            if i > new_list[0]:
                new_list[0] = i
        return(new_list[0])
    return(None)
