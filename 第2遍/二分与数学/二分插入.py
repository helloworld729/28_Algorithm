lst = [1, 2, 3, 4, 4, 4, 4, 5, 8]
def left_sect(value):
    l, r = 0, len(lst)-1
    while l < r:
        middle = l + (r-l) // 2
        if lst[middle] < value:
            l = middle + 1
        elif lst[middle] > value:
            r = middle - 1
        else:
            print(middle)
            return middle
    return l

# value = 4
# lst.insert(left_sect(value), value)



def left_insert(lst, value):
    l, r = 0, len(lst)-1
    while l <= r:
        middle = l + (r-l) // 2
        if lst[middle] < value:
            l = middle + 1
        else: r = middle - 1
    return l
print(left_insert(lst, 4))


# 小结：如果只是想找到或者插入，可以直接停止
# 如果想从最左边，或者最右边插入，那么遇到目标值不要停，直到循环自然结束

