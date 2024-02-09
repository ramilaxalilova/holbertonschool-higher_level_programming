#!/usr/bin/python3
"""class inheritance from class"""


class MyList(list):
    """for sorting class"""
    def print_sorted(self):
        print(sorted(self))
