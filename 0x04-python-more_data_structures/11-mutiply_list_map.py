#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    num_list = [number] * len(my_list)
    new_list = list(map(lambda x, y: x * y, my_list, num_list))
    return(new_list)
