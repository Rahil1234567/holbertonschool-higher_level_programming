#!/usr/bin/python3
def print_last_digit(number):
    lastdig = number % 10 if number >= 0 else -number % 10
    print("{}".format(lastdig), end="")
    return lastdig
