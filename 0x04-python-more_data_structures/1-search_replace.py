#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for x in range(len(my_list)):
        if my_list[x] == search:
            new_list[x] = replace
    return new_list
