"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
思路：partition操作，但是非稳定，不能保证原始顺序
"""
class Solution:
    def exchange(self, lst):
        if not lst: return lst
        l, r = 0, len(lst)-1
        pivot = lst[l]
        while l < r:
            while l < r and lst[r] % 2 == 0:  # odd
                r -= 1
            if l < r:
                lst[l] = lst[r]
                l += 1
            while l < r and lst[l] % 2 == 1:
                l += 1
            if l < r:
                lst[r] = lst[l]
                r -= 1
        lst[l] = pivot

        return lst