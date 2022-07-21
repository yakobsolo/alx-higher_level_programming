def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for x in new_dic:
        new_dic[x] = new_dic[x] * 2
    return new_dic
