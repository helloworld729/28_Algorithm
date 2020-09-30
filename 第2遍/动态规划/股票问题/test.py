class Solution:
    def maxProfit(self, k: int, prices) -> float:
        def infinity(prices):
            res = 0
            for i in range(1, len(prices)):
                res += max(0, prices[i] - prices[i-1])
            return res

        ll = len(prices)
        if ll < 2: return 0
        if k > ll // 2: return infinity(prices)

        dp = [[float("-inf") for i in range(2)] for j in range(1+k)]
        dp[0][0] = 0  # 唯一的base case
        for i in range(ll):
            # for j in range(1, min(1 + k, 1 + 1 + (1 + i) // 2)):  # 交易数目
            for j in range(1, 1+k):  # 交易数目
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])  # 终于空仓
                dp[j][1] = max(dp[j][1], dp[j-1][0]-prices[i])  # 终于持仓
        return max([i[0] for i in dp])

a = Solution()
lst = [3,3,5,0,0,3,1,4]
print(a.maxProfit(k=2, prices=lst))

# 0是空仓，1是持仓，从0到1是开始新交易，从1到0是完成本轮交易
# for j in range(1, min(1 + k, 1 + 1 + (1 + i) // 2)):  # 交易数目
# (1+i)转化为实际从1开始，加1因为第一天是可以完成1笔交易的持仓状态，再加1是因为右开区间



