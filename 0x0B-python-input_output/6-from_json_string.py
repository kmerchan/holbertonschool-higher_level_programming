#!/usr/bin/python3
"""defines function to return object from JSON"""


def from_json_string(my_str):
    """returns object from JSON"""
    import json
    return json.loads(my_str)
