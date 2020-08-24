#!/usr/bin/python3
"""
Python script to send request to given URL and display value of X-Request-Id
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        response = requests.get(argv[1])
        print(response.headers['X-Request-Id'])
    except Exception as err:
        pass
