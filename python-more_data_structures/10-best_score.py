#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxval = float('-inf')
    maxkey = None
    for key, val in a_dictionary.items():
        if val > maxval:
            maxval = val
            maxkey = key
    return maxkey
