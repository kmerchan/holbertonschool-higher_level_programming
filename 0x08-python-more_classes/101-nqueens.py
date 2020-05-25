#!/usr/bin/python3
"""defines program to solve the N queens problem"""


import sys
if len(sys.args) is not 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.args[1]
if type(N) is not int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
