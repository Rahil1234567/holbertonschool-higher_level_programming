#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import (add, sub, mul, div)

if __name__ == "__main__":
    try:
        if len(argv) != 4:
            print(f"Usage: {argv[0]} <a> <operator> <b>")
            exit(1)
        a = argv[1]
        b = argv[3]
        operator = argv[2]
        res = None
        if operator == '+':
            res = add(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '-':
            res = sub(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '*':
            res = mul(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '/':
            res = div(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    except Exception:
        exit(1)
