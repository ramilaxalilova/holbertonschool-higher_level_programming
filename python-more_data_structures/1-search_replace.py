#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list.copy()
    for i, item in enumerate(newl):
        if item == search:
            newl[i] = replace
    return newl
