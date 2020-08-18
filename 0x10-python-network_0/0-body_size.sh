#!/bin/bash
# sends request to given URL and displays the size of the body of response
if [ $# -lt 1 ]
then
    echo "Usage: 0-body_size.sh URL"
else
    curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
fi
