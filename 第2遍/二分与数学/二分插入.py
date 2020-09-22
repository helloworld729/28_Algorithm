lst = [1, 2, 3, 5, 8]
def left_sect(value):
    l, r = 0, len(lst)
    while l < r:
        middle = l + (r-l) // 2
        # 中小左进
        if lst[middle] < value:
            l = middle + 1
        else:
            r = middle
    return l

