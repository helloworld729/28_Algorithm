"""
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组
是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，
其中 n 也是一个整数。
输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
思路：用前缀和，如果一个区间[i:j]的和为K的倍数，那么s[i-1] s[j+1] 同余
其中将0的索引设为-1:有两个功能：当k为0，找和为0的位置，
2、开头就匹配即余数为0
"""
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if len(nums) < 2: return False
        dp, cur_sum = {0: -1}, 0  #　余数：索引

        for index, num in enumerate(nums):
            cur_sum += num  # 前缀和
            rest = cur_sum if k == 0 else cur_sum % k  # 求余数
            pre = dp.setdefault(rest, index)  # 上一个相同余数的索引
            if index - pre > 1: return True
        return False

"""
和为0的特殊处理：假如k为0的话，那么有一段区间的和为0，那么区间前后的前缀和相等，
    所以可以直接把前缀和作为余数记录。

"""

