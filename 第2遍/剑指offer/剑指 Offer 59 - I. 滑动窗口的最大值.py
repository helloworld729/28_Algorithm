from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        que = deque()
        res = []
        ll = len(nums)

        for i in range(ll):
            while que and que[-1][1] < nums[i]:
                que.pop()
            que.append((i, nums[i]))

            if i >= k-1:
                res.append(que[0][1])

            if que and i - que[0][0] >= k-1:
                que.popleft()

        return res
lst = [1, -1]
a = Solution()
print(a.maxSlidingWindow(lst, k=1))