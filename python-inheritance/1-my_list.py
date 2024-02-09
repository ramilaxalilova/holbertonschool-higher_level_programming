#!/usr/bin/python3
"""class inheritance from class"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
