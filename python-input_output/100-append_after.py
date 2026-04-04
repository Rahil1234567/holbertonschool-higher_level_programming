#!/usr/bin/python3
"""Manipulating a file."""


def append_after(filename="", search_string="", new_string=""):
    """Search and modify the lines containing search_string."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
            i += 2
        else:
            i += 1

    with open(filename, 'w', encoding='utf-8') as file:
        """Write the lines back into the file."""
        file.writelines(lines)
