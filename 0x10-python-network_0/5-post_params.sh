#!/bin/bash
# sends POST request to given URL for two variables & displays body of response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
