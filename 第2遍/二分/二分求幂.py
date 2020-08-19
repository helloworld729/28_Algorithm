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