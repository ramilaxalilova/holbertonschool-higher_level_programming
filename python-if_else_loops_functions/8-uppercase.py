#!/usr/bin/python3
def uppercase(str):
    char = ''
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
