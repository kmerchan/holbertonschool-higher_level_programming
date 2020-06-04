#!/usr/bin/python3
"""defines function to write JSON representatin of an object to file"""


def save_to_json_file(my_obj, filename):
    """write JSON representation of an object to a file"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
