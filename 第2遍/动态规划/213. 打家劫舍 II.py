# 环形列表的处理办法
class Solution:
    def rob(self, nums) -> int:
        """笨方法：数组切分为两类情况，分别调用函数，但是整体是O（N）的复杂度"""
        ll = len(nums)
        if not ll: return 0
        if ll < 4: return max(nums)

        lst_1 = nums[1:]
        lst_2 = nums[:ll]

        def max_rob(lst):
            dp = [0 for i in range(ll-1)]
            dp[0] = lst[0]
            dp[1] = max(lst[:2])
            for i in range(2, ll-1):
                dp[i] = max(dp[i-2]+lst[i], dp[i-1])
            return dp[-1]
        left, right = max_rob(lst_1), max_rob(lst_2)
        # print(left, right)
        return max(left, right)

