#!/usr/bin/python3
""" 4-from_json_string: from_json_string """
import json


def from_json_string(my_str):
    """
        Return:
            the python object
        Args:
            my_str: json string ready to be converted to python object
    """
    return json.loads(my_str)
