#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_set = set(my_list)
    new_list = list(new_set)
    for x in range(len(new_list)):
        sum = sum + new_list[x]
    return sum
