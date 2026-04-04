#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = ""
if number % 10 > 5:
    str = "and is greater than 5"
elif number % 10 == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
lastdig = number % 10 if number >= 0 else -((10 - number % 10) % 10)
print(f"Last digit of {number} is {lastdig}", str)
