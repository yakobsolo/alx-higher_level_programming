#!/usr/bin/python3
""" 6-load_from_json_file: load_from_json_file """
import json


def load_from_json_file(filename):
    """
    read json file
    Args:
        filename: contains a json file
    """
    with open(filename) as f:
        return json.load(filename)
