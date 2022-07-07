#!/usr/bin/python3
""" 5-save_to_json_file: save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """
    writes a object into json file
    Args:
        my_obj: python object
        filename: location to where we load the python object
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
