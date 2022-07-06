#!/usr/bin/python3
""" 1-write_file: def write_file """


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        Return:
            no of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
