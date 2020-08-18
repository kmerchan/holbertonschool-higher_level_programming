#!/bin/bash
# sends request to given URL and displays the size of the body of response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
