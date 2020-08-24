#!/usr/bin/python3
"""
Python script to send request to given URL and display value of X-Request-Id
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    if argv[1]:
        with request.urlopen(argv[1]) as response:
            print(response.getheader('X-Request-Id'))
