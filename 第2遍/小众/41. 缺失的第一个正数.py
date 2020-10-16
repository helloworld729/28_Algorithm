class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 首先判断1是否出现在list中
        if 1 not in nums: return 1

        # 转换为正数
        ll = len(nums)
        for i in range(ll):
            if nums[i] <= 0 or ll < nums[i]:
                nums[i] = 1

        # 标记
        for i in range(ll):
            index = abs(nums[i])
            nums[index - 1] = - abs(nums[index - 1])

        # 检测正数
        for i in range(ll):
            if nums[i] > 0:
                return 1 + i

        # 数值完整，返回下一个
        return 1 + ll

lst = [3, 1]
a = Solution()
print(a.firstMissingPositive(lst))

"""
思路：首先明确一个准则，返回值肯定在[1， ll+1]闭区间内  # 想想区间长度
为了满足时间O(N)空间O(1)的要求，处理如下：
1、检查1是否在list中，不在的话直接返回1；
2、将所有不在 [1， ll+1]之间的数置位1；
3、遍历每个位置的数，并在相应的位置做标记；
4、没有被标记的地方就是没有出现的数字；
"""