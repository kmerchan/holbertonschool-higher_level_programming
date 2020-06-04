#!/usr/bin/python3
"""defines function to return JSON representatin of an object"""


def to_json_string(my_obj):
    """returns JSON representation of an object"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
