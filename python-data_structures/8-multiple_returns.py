#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        char = None
    else:
        char = sentence[0]
    return length, char
