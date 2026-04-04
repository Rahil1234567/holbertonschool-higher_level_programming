#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        temp = a
        for i in range(b-1):
            a *= temp
        return a
    else:
        temp = a
        for i in range(-(b)-1):
            a *= temp
    return 1/a
