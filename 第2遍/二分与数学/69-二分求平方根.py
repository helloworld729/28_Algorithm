def sqrt(x):
    l, r, ans = 0, x, -1
    while l < r:
        mid = l + (r - l) // 2
        if mid ** 2 <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid
    return ans

for i in range(20): print(i, sqrt(i))
"""
求mid**2 < x 的最大mid值，所以用ans记录每一步的候选值
和二分插入是一个思路
"""

