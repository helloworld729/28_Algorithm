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
res为结果容器、一旦遇到奇数次方就抓下来一次，剩余偶数次方
偶次方处理方式：底数自乘，指数折半。
"""
