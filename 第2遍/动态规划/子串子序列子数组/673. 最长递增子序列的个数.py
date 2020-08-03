"""
给定一个未排序的整数数组，找到最长递增子序列的个数。
输入: [1,3,5,4,7]
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
与直接求最长上升子序列相比，要细分出长度关系
1、小于等于，一定是第一次遇到
2、长1：第二次遇到：第二次遇到同等段位的数字
"""

class Solution:
    def findNumberOfLIS(self, nums) -> int:
        ll = len(nums)
        if ll < 2: return ll
        counts = [1] * ll      # 以num[i]结尾的最长上升序列的 个数
        length = list(counts)  # 以num[i]结尾的最长上升序列的 长度
        max_len = 1  # 最长上升长度

        for i in range(ll):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] <= length[j]:  # 第一次遇到比自己低段位的某数字
                        length[i] = length[j] + 1
                        counts[i] = counts[j]
                    elif length[i] == length[j] + 1:  # 第二次遇到该段位的数字
                        counts[i] += counts[j]
                    max_len = max(max_len, length[i])

        res = 0
        for index in range(ll):
            if length[index] == max_len:
                res += counts[index]
        return res