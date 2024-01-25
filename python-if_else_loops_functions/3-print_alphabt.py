#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n == ord('q') or n == ord('e'):
        continue
    else:
        print("{:c}".format(n), end="")
