#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_list = [x % 2 == 0 for x in my_list]
    return final_list
