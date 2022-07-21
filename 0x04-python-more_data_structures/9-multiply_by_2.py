#!/usr/bin/pyton3
def multiply_by_2(a_dictionary):
    new_dic = dict()
    for x in a_dictionary:
        y = a_dictionary[x] * 2
        new_dic[x] = y
    return new_dic
