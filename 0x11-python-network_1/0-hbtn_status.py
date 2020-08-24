#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request as request
req = request.Request('https://intranet.hbtn.io/status')
response = request.urlopen(req)
print_content = response.read()
print("Body response:")
print("\t- type: {}".format("don't know"))
print("\t- content: {}".format(print_content))
print("\t- utf8 content: {}".format("don't know"))
