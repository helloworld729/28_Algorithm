"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

输入: [1,2,3,4,5]
输出: True
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
方法1：计数排序
方法2：快速排序
"""
class Solution:
    def isStraight(self, nums) -> bool:
        card = [0 for i in range(14)]
        for d in nums:
            card[d] += 1
            if card[d] > 1 and d != 0:
                return False
        zero_count = card[0]

        back = []
        for i in range(1, 14):
            if card[i]:
                back.append(i)

        gap = 0
        for i in range(1, len(back)):
            gap += back[i]-back[i-1]-1
        if gap <= zero_count:
            return True
        return False

    def isStraight2(self, nums) -> bool:
        import bisect
        nums.sort()
        zero_count = bisect.bisect_left(nums, 1)
        gap = 0
        for i in range(zero_count+1, 5):
            if nums[i] == nums[i-1]: return False
            gap += nums[i] - nums[i-1] -1
        if zero_count >= gap:
            return True
        return False



lst = [0,0,8,5,4]
a = Solution()
print(a.isStraight2(lst))