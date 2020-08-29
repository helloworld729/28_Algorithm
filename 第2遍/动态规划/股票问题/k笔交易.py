class Solution:
    def infinity(self, prices):
        ll = len(prices)
        res = 0
        for i in range(1, ll):
            interest = max(0, prices[i] - prices[i - 1])
            res += interest
        return res

    def maxProfit(self, k: int, prices):
        ll = len(prices)
        if ll < 2 or k == 0: return 0
        if k > ll // 2: return self.infinity(prices)

        dp = [[float("-inf") for _ in range(2)]for _ in range(k+1)]  # 注意1+k

        dp[1][1] = -prices[0]  # 如果k不加1而且k=1事后在这里会越界
        dp[0][0] = 0  # base case

        for i in range(1, ll):
            for j in range(1, k+1):
                dp[j][0] = max(dp[j][1] + prices[i], dp[j][0])
                dp[j][1] = max(dp[j-1][0]-prices[i], dp[j][1])

        return max([i[0] for i in dp])

a = Solution()
lst = [1,4]
print(a.maxProfit(1, lst))

"""
思路：首先题目中会有一个坑，就是k的值，正常的话，K的上限是ll//2，例如
ll=1, k最大为0
ll=2，K最大为1
那么假如k越界了呢，也就是说此时k是非法的k，例如只有4天的股票价格，但是K初始为5，那么
第一种思路把k变成2，继续用动规，第二种思路直接调用交易无限次的函数
思路1：时间O(KN)空间O(K)  
思路2：时间O(N)空间O(1)
所以选择思路2
动态规划：dp[i][j]:表示已经完成第i笔交易，而且状态为j获取的最大收益，j取值为0和1分别表示
          空仓和持仓
                dp[j][0] = max(dp[j][1] + prices[i], dp[j][0])
                dp[j][1] = max(dp[j-1][0]-prices[i], dp[j][1])
          假如没有进行状态压缩的话，最初的动规为：
                dp[i][j][0] = max(dp[i-1][j][1] + prices[i], dp[i-1][j][0])
                dp[i][j][1] = max(dp[i-1][j-1][0]-prices[i], dp[i-1][j][1])
          我们可以发现：i来自于直接前驱可以去掉
"""