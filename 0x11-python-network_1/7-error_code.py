#!/usr/bin/python3
"""
Python script to send request to given URL
and display body of response, decoded
also handles error is HTTP status code is >= 400
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
