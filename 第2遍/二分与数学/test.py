# 快速求幂
def mypow(num, n):
    if n < 0: num, n = 1/num, -n
    res = 1
    while n > 0:
        if n & 1: res *= num
        num *= num
        n >>= 1
    return res

for i in range(1, 5):
    print(mypow(i, 2))

