"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

"""

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        """2000ms 5% 四个状态分别表示 持仓卖出， 持仓无操作， 空仓买入， 空仓无操作"""
        ll = len(prices)
        if ll < 2: return 0

        dp = [[0 for _ in range(4)] for _ in range(ll)]
        dp[0][0], dp[0][1], dp[0][2] = float("-inf"), float("-inf"), -prices[0]

        for i in range(1, ll):
            increase = prices[i]-prices[i-1]

            dp[i][0] = max(dp[i-1][1]+increase-fee, dp[i-1][2]+prices[i]-fee)  # right
            dp[i][1] = max(dp[i-1][1]+increase,     dp[i-1][2]+prices[i])      # right
            dp[i][2] = max(dp[i-1][0]-prices[i],    dp[i-1][3]-prices[i])      # right
            dp[i][3] = max(dp[i-1][0],              dp[i-1][3])                # right

        return max(dp[-1][0], dp[-1][3])

    def maxProfit2(self, prices, fee: int) -> int:
        """1504ms  5% 虽然钱少了，但是换成了等价的黄金在手里，最后卖了，
        所以对购买而言，是不用付一个price的  两个状态分别是空仓和持仓"""
        ll = len(prices)
        if ll < 2: return 0
        dp = [[0 for _ in range(2)] for _ in range(ll)]
        dp[0][0], dp[0][1] = 0, 0
        for i in range(1, ll):
            increase = prices[i]-prices[i-1]
            dp[i][0] = max(dp[i-1][0],            dp[i-1][1]+increase-fee)  # right
            dp[i][1] = max(dp[i-1][0],            dp[i-1][1]+increase)      # right
        return dp[-1][0]

    def maxProfit3(self, prices, fee: int) -> int:
        """1016ms 58% 优化空间后，提速了很多"""
        ll = len(prices)
        if ll < 2: return 0
        empty, hold = 0, 0
        for i in range(1, ll):
            new_hold = prices[i]-prices[i-1] + hold
            empty_back = empty
            empty = max(empty,  new_hold-fee)  # right
            hold =  max(empty_back,  new_hold)      # right
        return empty

a = Solution()
price = [1, 3,5]
fee = 2
print(a.maxProfit2(price, fee))