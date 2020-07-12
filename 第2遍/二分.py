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

# ########################## 二分求幂 leetcode-50 ######################################
def cal_pow(x, n):  # n>0的整数
    if n == 1:
        return x
    if n % 2 == 0:
        ans = cal_pow(x, n/2)
        return ans * ans
    else:
        ans = cal_pow(x, n//2)
        return ans * ans * x
print(cal_pow(2, 3))
# print(cal_pow(2.1,3))

# from collections import defaultdict
# while True:
#     back_dict = defaultdict(str)
#     s = input()
#     for char in s:
#         if back_dict[char]==1:  # 已经有的话
#             pass
#         else:
#             back_dict[char] = 1  # 新的
#     for key in list(back_dict.keys()):
#         print(key,end='')
