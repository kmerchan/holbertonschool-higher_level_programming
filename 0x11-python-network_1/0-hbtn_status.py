#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        utf8_content = content.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
