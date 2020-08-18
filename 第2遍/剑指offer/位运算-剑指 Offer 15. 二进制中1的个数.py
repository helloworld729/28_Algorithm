class Solution:
    def hammingWeight(self, n: int) -> int:
        """逐位判断"""
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def hammingWeight2(self, n: int) -> int:
        """巧用n(n-1)"""
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
