#!/usr/bin/python3
for i in range(100):
    if "{:02d}".format(i)[0] == "{:02d}".format(i)[1]:
        continue
    elif "{:02d}".format(i)[0] > "{:02d}".format(i)[1]:
        continue
    else:
        print("{:02d}".format(i), end=", " if i != 89 else "\n")
