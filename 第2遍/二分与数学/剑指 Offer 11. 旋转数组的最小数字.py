lst = [3, 3, 1, 2]
ll = len(lst)
l, r = 0, ll-1
mid = r - (r-l)//2
while mid < r:
    if lst[mid] <= lst[l]:
        r = mid
    elif lst[mid] >= lst[l]:
        l = mid
    mid = r - (r-l)//2
print(lst[mid])