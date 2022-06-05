#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx <= len(my_list) - 1:
        ins = my_list[:]
        ins[idx] = element
        return ins
    else:
        return my_list
