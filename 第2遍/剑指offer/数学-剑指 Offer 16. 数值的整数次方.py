"""
不得使用库函数，同时不需要考虑大数问题。 
输入: 2.00000, 10
输出: 1024.00000
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof

方法1：二分求幂
方法2：位运算求解
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow_(x, y):
            if y == 0: return 1
            if y == 1: return x
            else:
                half = pow_(x, y // 2)
                if y %2 == 0:
                    return half * half
                else:
                    return half * half * x

        if n > 0: return pow_(x, n)
        return 1/pow_(x, -n)

    def myPow2(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res