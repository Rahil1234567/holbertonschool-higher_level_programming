#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum = 0
    my_list = list(set_list)
    for i in range(len(my_list)):
        sum += my_list[i]
    return sum
