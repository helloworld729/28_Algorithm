class Solution:
    def maxProfit(self, k: int, prices) -> int:
        N = len(prices)
        if N < 2: return 0
        dp = [[float("-inf") for _ in range(k+1)] for _ in range(N)]
        dp[0][0] = 0
        mini_num = prices[0]
        for i in range(1, N):
            for v in range(k, 0, -1):
                increase = prices[i]-prices[i-1]
                if v == 1:
                    dp[i][v] = max(dp[i-1][v], prices[i]-mini_num)
                else:
                    may = dp[i-2][v-1]+prices[i]-prices[i-2] if i>=2 else float("-inf")
                    dp[i][v] = max(dp[i-1][v], dp[i-1][v-1]+increase, may)
            mini_num = min(mini_num, prices[i])
        for da in dp:
            print(da)
        return max(0, max(dp[-1]))
prices = [6,1,3,2,4,7]
k=2
a = Solution()
print(a.maxProfit(k, prices))
