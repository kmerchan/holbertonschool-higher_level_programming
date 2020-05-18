#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0]*list_length
    for i in range(list_length):
        try:
            new_list[i] = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
    return new_list
