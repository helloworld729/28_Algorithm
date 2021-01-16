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
        prefix = {0: -1}

        temp_sum = 0
        for index, data in enumerate(nums):
            temp_sum += data
            rest = temp_sum if k == 0 else temp_sum % k

            if rest in prefix:
                pre = prefix[rest]
                if index - pre >= 2:return True
            else:
                prefix[rest] = index

            return False



"""
1、和为0的特殊处理：假如k为0的话，那么有一段区间的和为0，那么区间前后的前缀和相等，
所以可以直接把前缀和作为余数记录。
    
2、为什么预设 余数为0在-1呢？假设刚好前两个数就满足要求，那么由于没有pre这个参数
所以要预设

3、假设前缀和取余已经为i，然后至少出现了两个数 a, b 这时候前缀和取余仍然是i
所以index 距离大于等于2

"""

