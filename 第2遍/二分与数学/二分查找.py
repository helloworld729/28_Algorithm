def half_asc(lst, target):
    l, r = 0, len(lst)
    while l < r:
        middle = l + (r - l) // 2
        if lst[middle] == target:
            return True
        elif lst[middle] < target:
            l = middle + 1  # key-point
        elif lst[middle] > target:
            r = middle
    return False

def half_dec(lst, target):
    l, r = 0, len(lst)
    while l < r:
        mid = l + (r-l) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            l = mid + 1
        else:
            r = mid
    return False

# 场景：判断一个数有没有出现在lst中
# 升序查找：中小左进，中大右回
# 降序查找：中大左进，中小右回

