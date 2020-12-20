class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  # 13
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  # 13
        res = ""
        pos = 0
        while True:
            flag = True
            for i in range(pos, len(nums)):
                counts = num // nums[i]
                if counts != 0:
                    res += strs[i] * counts
                    num -= nums[i] * counts
                    flag = False
                    pos = i + 1
                    break
            if flag: break
        return res

"""
题目：https://leetcode-cn.com/problems/integer-to-roman/
"""

