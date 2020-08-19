"""
统计一个数字在排序数组中出现的次数。
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
"""
class Solution:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):  # 查找插入的右边界
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2  # 向下取整
                if nums[m] <= tar: i = m + 1  # 中指在右侧
                else: j = m - 1  # 中指在左侧
            return i
        return helper(target) - helper(target - 1)

