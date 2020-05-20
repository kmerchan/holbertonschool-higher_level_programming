#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("1--2")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("2--3")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("3--4")

my_square_4 = Square()
my_square_4.size = 0
my_square_4.position = (5, 5)
my_square_4.my_print()

print("4--5")

my_square_5 = Square(2, (1, 1))
my_square_5.size = 1
my_square_5.position = (5, 5)
my_square_5.my_print()

print("5--6")

my_square_6 = Square(2, (1, 1))
try:
    my_square_6.size = 1
except Exception as e:
    print(e)
try:
    my_square_6.position = (-5, "5")
except Exception as e:
    print(e)
my_square_6.my_print()

print("--")
