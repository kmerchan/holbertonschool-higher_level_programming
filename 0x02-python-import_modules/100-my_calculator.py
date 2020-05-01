#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args_list = sys.argv[1:]
    if len(args_list) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(args_list[0])
    b = int(args_list[2])
    if args_list[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args_list[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args_list[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args_list[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
