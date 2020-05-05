#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + tuple_c
    if len(tuple_b) < 2:
        tuple_b = tuple_b + tuple_c
    value1 = tuple_a[0] + tuple_b[0]
    value2 = tuple_a[1] + tuple_b[1]
    tuple_d = (value1, value2)
    return(tuple_d)
