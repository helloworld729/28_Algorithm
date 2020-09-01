# ########################## 二分求幂 leetcode-50 ######################################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 算法主流程是按照偶数分析，如果是奇数就转化为奇数
        if x == 0: return 0
        if n == 0: return 1
        if n < 0: x, n = 1/x, -n

        res = 1
        while n > 0:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

"""
pow(x, n) = pow(x*x, n//2)  # n为偶数
因为n除以2相当于右移一位，最终会等于1，此时把结果转移到res
如果n是奇数的话，先把x乘到res上，n变成偶数
"""
