#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
max_value = max_integer()
print("Max: {}".format(max_value))
new_list = [-1, -2, -3, -4]
max_value = max_integer(new_list)
print("Max: {}".format(max_value))
