#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    value = 0
    i = 0

    if isinstance(roman_string, str):
        while i < len(roman_string):
            if (
                i + 1 < len(roman_string)
                and roman_values[roman_string[i]] <
                roman_values[roman_string[i + 1]]
            ):
                value += (roman_values[roman_string[i + 1]] -
                          roman_values[roman_string[i]])
                i += 2
            else:
                value += roman_values[roman_string[i]]
                i += 1
        return value
    else:
        return 0
