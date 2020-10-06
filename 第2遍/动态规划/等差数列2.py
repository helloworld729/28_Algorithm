from typing import *
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        maps = [defaultdict(int) for _ in range(n)]
        total = 0
        for i in range(1, n):   # 结尾元素索引
            for j in range(i):  # A[i]-A[j]为公差
                # 弱等差数列的个数，至少为1，因为任意两个数都是一个等差数列
                add_val = (maps[j][A[i]-A[j]]+1)
                maps[i][A[i]-A[j]] += add_val
                total += add_val - 1
        print(maps)
        return total


if __name__ == '__main__':
    a = Solution()
    lst = [1, 2, 3, 4, 5, 6]
    print(a.numberOfArithmeticSlices(lst))


"""
map[i][j]表示以A[i]结尾的公差为j的等差数列的个数
弱等差数列：长度为2的等差数列，目的是为了去掉边界处理
"""