#!/usr/bin/python3
"""defines class Student"""


class Student():
    """class to define student"""

    def __init__(self, first_name, last_name, age):
        """initializes student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary descript for JSON serialization"""
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            if key is first_name:
                self.first_name = json[key]
            if key is last_name:
                self.last_name = json[key]
            if key is age:
                self.age = json[key]
