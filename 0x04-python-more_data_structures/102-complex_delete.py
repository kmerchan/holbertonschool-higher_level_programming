#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        check = False
        for k, v in a_dictionary.items():
            if v == value:
                check = k
        if check:
            del a_dictionary[check]
            return(complex_delete(a_dictionary, value))
    return(a_dictionary)
