"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        dp = [0] * (n+1)
        dp [0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1] % (pow(10, 9)+7)

    def fib2(self, n: int) -> int:
        """优化空间复杂度"""
        if n == 0: return 0
        if n == 1: return 1
        a, b = 0, 1
        for i in range(n//2):
            a = a+b
            b = a+b
        c = b if n & 1 else a
        return c % (pow(10, 9)+7)

    def fib3(self, n: int) -> int:
        """优化空间复杂度"""
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b  # a的更新对b本次更新没有影响
        return a % (pow(10, 9)+7)
