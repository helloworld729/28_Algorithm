def half_asc(lst, target):
    l, r = 0, len(lst)-1
    while l <= r:
        middle = l + (r - l) // 2
        if lst[middle] == target:
            return True
        elif lst[middle] < target:
            l = middle + 1  # key-point
        elif lst[middle] > target:
            r = middle - 1
    return False

def half_dec(lst, target):
    l, r = 0, len(lst)-1
    while l < r:
        mid = l + (r-l) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            l = mid + 1
        else:
            r = mid - 1
    return False

# 二分问题思路：边界值约定为可以取到的，然后中值先判断，
# 假如中值不是的话target大说明右边界太大，r=mid-1，这里
# 可以mid-1是因位mid已经判断过了。

def half_search(lst, num):
    l, r = 0, len(lst) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            l = mid + 1
        else:
            r = mid -1
    return None

print(half_search([1,4,4,5], 4))


