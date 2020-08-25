#!/usr/bin/python3
"""
Python script to list 10 most recent commits
to repository 'rails' by user 'rails'
using GitHub API
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    response = requests.get(url)
    json_list = response.json()
    count = 0
    for obj in json_list:
        if count == 10:
            break
        print("{}: {}".format(
            obj.get('sha'),
            obj.get('commit').get('author').get('name')))
        count = count + 1
