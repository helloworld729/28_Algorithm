"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof

思路：分组亦或。分组依据:在某一位为0还是为1.哪一位呢？a, b不相同的位置。
"""
class Solution:
    def singleNumbers(self, nums):
        ret = 0
        for d in nums:
            ret ^= d

        tech = 1
        # 注意：这个地方不能用 ！= 1 判断，因为
        # 一旦等于1了，就卡住了
        while ret & tech == 0:
            tech <<= 1

        a, b = 0, 0
        for d in nums:
            if d & tech:
                a ^= d
            else:
                b ^= d
        return [a, b]



