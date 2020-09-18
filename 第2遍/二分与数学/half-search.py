lst = [1, 2, 3, 5, 8]
def left_sect(value):
    l, r = 0, len(lst)
    while l < r:
        middle = l + (r-l) // 2
        # 左边界有效推进
        if value > lst[middle]: l = middle + 1
        else: r = middle
    return l

# for num in range(10):
#     pos = left_sect(num)
#     lst.insert(pos, num)
#     print(pos, lst)

# ########################################################################
lst = []
def reverse_half(value):
    l, r = 0, len(lst)
    while l < r:
        middle = l + (r-l) // 2
        if value < lst[middle]:
            l = middle + 1
        else: r = middle
    return l

for num in range(10):
    pos = reverse_half(num)
    lst.insert(pos, num)
    print(pos, lst)