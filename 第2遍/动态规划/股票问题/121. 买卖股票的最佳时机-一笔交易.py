"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），
设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）
的时候卖出，最大利润 = 6-1 = 5 。 注意利润不能是 7-1 = 6, 因为卖出
价格需要大于买入价格；同时，你不能在买入前卖出股票。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

实际上是求一个最大差值，刚开始用最长上升子序列的思路，超时了
后来发先将dp[I]记作至此的最低价格即可
"""
class Solution:
    def maxProfit(self, prices) -> int:
        """DP首先定义 到当前日期的最低股票价格，然后对差值去一个最大贪心 O(N)"""
        ll = len(prices)
        if ll <= 1: return 0
        res = 0
        dp = list(prices)  # 最低价格
        for i in range(1, ll):
            dp[i] = min(dp[i-1], prices[i])
            res = max(res, prices[i] - dp[i])
        return res
