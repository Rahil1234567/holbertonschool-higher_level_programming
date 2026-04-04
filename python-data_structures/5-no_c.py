#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join([a for a in my_string if a != 'c' and a != 'C'])
    return my_string
