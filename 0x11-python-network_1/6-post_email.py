#!/usr/bin/python3
"""
Python script to send POST request to given URL with given email as parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    if argv[2]:
        data = {}
        data['email'] = argv[2]
    if argv[1]:
        response = requests.post(argv[1], data)
        content = response.text
        print(content)
