"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
客观上，还是想求一个最长单调不减的区间，但是由于无序，所以先排序
与最长上升子序列的区别在于，不要求按照原来的顺序单调不减，而是不
重叠。是有区别的，不能直接套用。

dp[i]:i个区间之前(包括i)的最多互不重叠区间的个数
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        ll = len(intervals)
        if ll < 2: return 0
        dp = [1] * ll
        max_len = 1

        intervals.sort(key=lambda x: x[1])

        for i in range(ll):
            # 区间j的右边界 小
            for j in range(i-1, -1, -1):
                # 如果区间i的左边界>区间j的右边界，那么长度加1，并且停止搜索
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
            # 假如没有搜寻到，那么保证随着i的增大，分立区间数不减
            dp[i] = max(dp[i], dp[i-1])
            max_len = max(max_len, dp[i])

        return ll - max_len

    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length <= 1: return 0
        # 按照左边界、区间长度排序
        intervals.sort(key=lambda x: (x[0], x[1] - x[0]))

        # 分立区间数目
        count = 0
        # 右边界
        right = float("-inf")

        for i in range(length):
            if not count or intervals[i][0] >= right:
                count += 1
                right = intervals[i][1]
            elif intervals[i][1] < right:
                right = intervals[i][1]

        return length - count

    # 贪心：希望当前不重叠区间的右边界尽量小
    # 首先排序后 如果新区间在不重叠右侧，直接加入
    # 否则 如果新区间的右边界小 则替换。
    # 类似的还有最长上升子序列
