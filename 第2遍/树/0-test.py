"""
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
方法：移除比当前元素小的所有元素，因为当前元素的索引最靠后，不会造成误删的后果
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res, que = [], deque()
        ll = len(nums)

        if not ll & k: return []
        if k == 1: return nums

        for i in range(ll):
            if que and i - que[0] >= k:que.popleft()
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)
            res.append(nums[que[0]])
        return res[k-1:]

nums = [1,3,-1,-3,5,3,6,7]
a = Solution()
print(a.maxSlidingWindow(nums, 3))