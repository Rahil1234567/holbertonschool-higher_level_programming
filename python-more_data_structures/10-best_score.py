#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best = list(a_dictionary.values())[0]
        for value in a_dictionary.values():
            if value > best:
                best = value
        for key, value in a_dictionary.items():
            if value == best:
                return key
