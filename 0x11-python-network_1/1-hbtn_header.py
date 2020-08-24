#!/usr/bin/python3
"""
Python script to send request to given URL and display value of X-Request-Id
"""
from urllib import request
from sys import argv
if argv[1] is not None:
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
