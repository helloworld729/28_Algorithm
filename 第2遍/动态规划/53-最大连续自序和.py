# ########################## 最大连续子序和 leetcode-53 ######################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """O(N) O(1)"""
        current_sum, max_sum = float("-inf"), float("-inf")
        for data in nums:
            if current_sum < 0:  # 小于零，无条件换边界
                current_sum = data
            else: current_sum += data
            max_sum = max(max_sum, current_sum)
        return max_sum

    def maxSubArray2(nums) -> int:
        """
        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        状态转移：只有前串为正时，才将其和自己划在一起
        O(N) O(N)
        """
        dp = list(nums)  # 浅拷贝
        for i in range(1, len(dp)):
            if dp[i - 1] > 0:  # 状态转移
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)
