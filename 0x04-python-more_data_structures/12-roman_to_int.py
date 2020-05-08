#!/usr/bin/python3
def roman_to_int(roman_string):
    if not(roman_string):
        return(0)
    if type(roman_string) != str:
        return(0)
    value = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(roman_string)):
        for x, y in convert.items():
            if i != len(roman_string) - 1:
                if roman_string[i] == x:
                    for x2, y2 in convert.items():
                        if roman_string[i+1] == x2:
                            if y2 > y:
                                value -= y
                            else:
                                value += y
            else:
                if roman_string[i] == x:
                    value += y
    return(value)
