#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maximum_value = my_list[0]
    for i in my_list:
        if i > maximum_value:
            maximum_value = i
    return maximum_value
