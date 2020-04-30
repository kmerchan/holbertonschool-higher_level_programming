#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    summation = 0
    argument_list = sys.argv[1:]
    for argument in argument_list:
        summation += int(argument)
    print("{}".format(summation))
