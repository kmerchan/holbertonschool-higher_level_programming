#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    c = False
    for k in a_dictionary:
        if k == key:
            c = True
    if c:
        del a_dictionary[key]
    return(a_dictionary)
