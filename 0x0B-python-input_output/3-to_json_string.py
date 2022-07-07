#!/usr/bin/python3
""" 3-to_json_string: to_json_string """
import json


def to_json_string(my_obj):
    """
        Return:
            returns the json file
        Args:
            my_obj: ready object to convert to json string
    """
    return json.dumps(my_obj)
