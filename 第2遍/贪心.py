"""
贪心的解题思路：
"""
# 最大子串和 53
def maxSubArray(nums):
    """
        来源：https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode/
        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        思路：current_sum:在每一个位置都做一次决策：衔接到前面成串还是独立出来，从我开始?比较两种选择的值
        通俗：见到肉就吃，见到垃圾就躲开。
    """
    n = len(nums)
    curr_sum = max_sum = nums[0]

    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i])  # 贪心决策
        max_sum = max(max_sum, curr_sum)

    return max_sum


