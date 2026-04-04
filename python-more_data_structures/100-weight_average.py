#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum = 0
        weight = 0
        for pairs in my_list:
            sum += pairs[0] * pairs[1]
            weight += pairs[1]
        return sum / weight
    else:
        return 0
