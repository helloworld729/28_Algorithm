# 题目：https://leetcode-cn.com/problems/sorted-matrix-search-lcci/
# 在一个有序矩阵中找是否有目标值
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def half_search(lst, target):
            l, r = 0, len(lst)
            while l < r:
                middle = l + (r - l) // 2
                if lst[middle] == target:
                    return True
                elif lst[middle] < target:
                    l = middle + 1  # key-point
                elif lst[middle] > target:
                    r = middle
            return False

        ll = len(matrix)
        if not ll or not matrix[0]: return False

        for i in range(ll):
            if matrix[i][-1] < target:
                continue
            if half_search(matrix[i], target):
                return True
        return False

# 时间复杂度：NlogN
# 空间复杂度：O(1)