class Solution:
    def superPow(self, a: int, b) -> int:
        base = 1337
        if not b: return 1

        last = b.pop()
        part1 = (a ** last) % base
        part2 = (self.superPow(a, b) ** 10) % base

        return (part1 * part2) % base


"""
那么，说一个关于模运算的技巧吧，毕竟模运算在算法中比较常见：
(a * b) % k = (a % k)(b % k) % k
证明很简单，假设：a = Ak +B；b = Ck + D
"""