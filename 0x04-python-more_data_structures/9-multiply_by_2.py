def multiply_by_2(a_dictionary):
    new_dic = dict()
    for x in a_dictionary:
        new_dic[x] = a_dictionary[x] * 2
    return new_dic
