#!/usr/bin/python3
"""
Python script to send request to given URL
and display body of response, decoded
also handles urllib.error.HTTPError exception
"""
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            content = response.read()
            utf8_content = content.decode("UTF-8")
            print(utf8_content)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
