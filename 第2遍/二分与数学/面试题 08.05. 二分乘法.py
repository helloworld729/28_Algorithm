class Solution:
    def multiply(self, A: int, B: int) -> int:
        a, n = max(A, B), min(A, B)
        res = 0
        while n > 0:
            if n & 1: res += a
            a += a
            n >>= 1
        return res


"""
模拟5 * 3
5 * 3 = 5 * 2 + 5
a  n  res
5  3  0
5  2  5
10 1  5
20 0  15
如果n是奇数，我们在res中把被乘数加上，余项
继续计算。res是一个工具包。res+a后，n之所以
不用减去1，因为当前是奇数，接着是右移，不必。
"""
