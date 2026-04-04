#!/usr/bin/python3
count = 122
while count > 96:
    if count % 2 == 0:
        print("{}".format(chr(count)), end='')
        count -= 1
    elif count % 2 == 1:
        print("{}".format(chr(count - 32)), end='')
        count -= 1
