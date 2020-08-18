#!/bin/bash
# displays all HTTP methods the server at given URL will accept
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
