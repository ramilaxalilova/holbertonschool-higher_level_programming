
    n = len(list)
    if n==0 and n==1:
        return True
    if list[0]<list[1]: return verify_is_sorted(list[1:])