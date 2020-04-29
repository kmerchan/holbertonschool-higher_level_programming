#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ""
    if n > len(str) or n < 0:
        strcopy = str
        return(strcopy)
    for i in range(n):
        strcopy = strcopy + str[i]
    for i in range(n + 1, len(str)):
        strcopy = strcopy + str[i]
    return(strcopy)
