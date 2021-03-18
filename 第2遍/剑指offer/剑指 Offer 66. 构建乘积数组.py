from typing import List
# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中B[i] 的值是数组 A 中
# 除了下标i以外的元素的积, 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        length = len(a)
        if length <= 1: return []

        left = [1]
        for i in range(1, len(a)):
            left.append(left[-1] * a[i - 1])

        right = [1]
        for i in range(length - 2, -1, -1):
            right.append(right[-1] * a[i + 1])

        res = []
        for i in range(length):
            res.append(left[i] * right[length - 1 - i])
        return res

        # 时间O(N), 空间O(N)

