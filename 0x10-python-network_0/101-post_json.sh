#!/bin/bash
# sends POST request with JSON file to given URL and displays response
curl -sF "data=$2" "$1"
