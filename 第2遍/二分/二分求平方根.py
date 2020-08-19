# 第一题 2分法求平方根取整-69
def sqrt(x):
    if x < 2:
        return x
    l, r = 0, x
    while l < r:
        mid = int(0.5*(l + r))
        if mid * mid == x:
            return  mid
        elif mid * mid < x:
            l = mid
        else:
            r =mid
        if l + 1 == r:
            return l
# for i in range(20):
#     print(sqrt(i))


