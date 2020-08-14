"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""
class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix: return False
        r, c = len(matrix), len(matrix[0])
        if not r*c: return False
        color = float("inf")

        def dfs(i, j):
            if not (0 <= i <= r-1 and 0 <= j <= c-1):
                return False
            if target == matrix[i][j]:
                return True
            if matrix[i][j] > target:
                return False
            matrix[i][j] = color
            return dfs(i, j+1) or dfs(i+1, j)

        return dfs(0, 0)
