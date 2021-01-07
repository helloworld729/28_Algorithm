from typing import List
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ll = len(A)
        if ll < 2: return 0

        left = [0] * ll
        right = [0] * ll
        for i in range(1, ll):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(ll - 2, 0, -1):
            if A[i] > A[i + 1]:
                right[i] = right[i + 1] + 1

        res = 0
        for i in range(1, ll):
            if left[i] and right[i]:  # 两个都比中间低才可以
                res = max(res, left[i] + right[i] + 1)
        return res if res >= 3 else 0

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = Solution()
print(a.longestMountain(lst))


"""
"山脉"就是左边严格小，右边严格大，返回最长的山脉长度或者0
长度不小于3。
"""