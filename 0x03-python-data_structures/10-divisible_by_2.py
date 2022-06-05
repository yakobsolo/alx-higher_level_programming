#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == 0:
        return None
    bol_lis = []
    for i in my_list:
        if i % 2 == 0:
            bol_lis.append(True)
        else:
            bol_lis.append(False)
    return bol_lis
