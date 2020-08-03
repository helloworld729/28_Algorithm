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
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        ll = len(intervals)
        if ll < 2: return 0
        dp = [1] * ll
        max_len = 1

        intervals.sort(key=lambda x: x[1])

        for i in range(ll):
            for j in range(i-1, -1, -1):
                # 如果区间i的左边界>区间j的右边界，那么长度加1
                # 又因为排了序，前面不会有再长的上升区间长度，所以berak
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
            dp[i] = max(dp[i], dp[i-1])
            max_len = max(max_len, dp[i])

        return ll - max_len