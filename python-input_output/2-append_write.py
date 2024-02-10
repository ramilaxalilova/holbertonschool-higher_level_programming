#!/usr/bin/python3
"""apend new txt"""


def append_write(filename="", text=""):
    """Writes a string to a text file and returns len"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
