"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
输入: [10,2]
输出: "102"
"""
import functools
class Solution:
    def minNumber(self, nums) -> str:
        # 为什么呢？因为一个数除以同级别的9会得到一个以自身为循环节的无限循环
        temp = sorted(nums,key=lambda x:x/(pow(10, len(str(x)))-1))  # 以21为例，这里是除以99，而不是10
        return ''.join(map(str,temp))


    def minNumber2(self, nums):
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

a = Solution()
print(a.minNumber2([21, 221]))