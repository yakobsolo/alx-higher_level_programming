#!/usr/bin/python3
""" 2-append_write: def append_write """


def append_write(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        Return:
            no of characters that are been added
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write('\n')
        return f.write(text)
