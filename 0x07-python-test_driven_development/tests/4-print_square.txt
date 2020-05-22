============================
doctest for 4-print_square.py
============================
``print_square()`` prints square of given size with "#" character

TEST CONDITIONS
===============

testing printing a square of int size
::
>>> print_square = __import__('4-print_square').print_square
>>> print_square(2)
##
##

testing printing a square of size 0
::
>>> print_square(0)

testing no size argument
::
>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'

testing None argument
::
>>> print_square(None)
Traceback (most recent call last):
TypeError: size must be an integer

testing negative size argument
::
>>> print_square(-4)
Traceback (most recent call last):
ValueError: size must be >= 0

testing float argument
::
>>> print_square(3.14159)
Traceback (most recent call last):
TypeError: size must be an integer

testing string argument
::
>>> print_square("9")
Traceback (most recent call last):
TypeError: size must be an integer
