#!/bin/bash
# sends GET request to given URL and displays only the status code of response
curl -sI "$1" -o /tmp/output -w '%{http_code}'
