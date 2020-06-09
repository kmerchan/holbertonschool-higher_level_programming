#!/usr/bin/python3
"""defines Base class"""


class Base():
    """manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes to given id or
        increases class nb_objects and sets as default id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list of dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representaiton of
        list of instances who inherits from Base to a file"""
        if list_objs is None:
            list_objs = []
        if str(cls) == "<class 'models.rectangle.Rectangle'>":
            cls_name = "Rectangle"
        if str(cls) == "<class 'models.square.Square'>":
            cls_name = "Square"
        filename = cls_name + ".json"
        list_dictionaries = []
        for instance in list_objs:
            list_dictionaries.append(instance.to_dictionary())
        with open(filename,'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        for list of dictionaries"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
