class Solution:
    def superPow(self, a: int, b) -> int:
        base = 1337
        if not b: return 1

        last = b.pop()
        part1 = (a ** last) % base
        part2 = (self.superPow(a, b) ** 10) % base

        return (part1 * part2) % base


"""
积的模=模的积的模
(a * b) % k = (a % k)(b % k) % k 
证明很简单，假设：a = Ak +B；b = Ck + D
"""