# ############################## 239. 滑动窗口最大值 ##############################
"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。你能在线性时间复杂度内解决此题吗？
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
链接：https://leetcode-cn.com/problems/sliding-window-maximum
单调队列为什么可以？：假如直接返回窗口的最大值，那么复杂度为O（N-1）(K-1)=O(NK)
采用单调队列，使得队列中的数始终单调递减，每个数据最多入队一次，出队一次,复杂度为O(N)
单调队列范式：
1、判断最大值索引是否越界：if que and l > que[0]: que.popleft()
2、先把当前值和队列末端比较，清楚小数
3、假如队列没有满，把当前数压入
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)  # 处理特殊情况，可以降低时间
        if n * k == 0: return []
        if k == 1: return nums

        res, que, r = [], deque(), 0        # 返回容器，单调队列，右边界初始化
        for l in range(n - k + 1):  # 左边界推进
            if que and l > que[0]: que.popleft()
            while r < l + k:                      # 只在第一次会循环多次，后面只会一次
                cans = nums[r]
                if que and cans > nums[que[-1]]:  # 先把小数干掉
                    while que and cans > nums[que[-1]]:
                        que.pop()
                # 全部干掉了，或者当前值不是最大的，但是窗口未满(下一轮就可能最大了，所以要保存)
                if len(que) < k: que.append(r)
                r += 1
            res.append(nums[que[0]])
        return res
