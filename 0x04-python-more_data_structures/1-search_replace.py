#!/usr/bin/python3
""" 1-search_replace: def search_replace """
def search_replace(my_list, search, replace):
    """
        search and replace a value
        Args:
            my_list:
            search:
            replace:
        Return: 
            the newly replaced list
    """
    new_list = list(my_list)
    for x in range(len(my_list)):
        if my_list[x] == search:
            new_list[x] = replace
    return new_list
