# 允许无限次交易、每一笔交易有固定的手续费
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        ll = len(prices)
        if ll < 2: return 0
        empty, hold = 0, -prices[0]
        for i in range(1, ll):
            empty = max(empty, hold + prices[i] - fee)
            hold  = max(hold, empty-prices[i])
        return empty

a = Solution()
price = [1, 3, 2, 8, 4, 9]
fee = 2
print(a.maxProfit(price, fee))

# 加不加temp结果都可以通过?
# 加临时变量肯定不会错，问题是可不可以不加，分析后发现真的可以不加
# 因为empty可能在8行改变，但是只要empty取后者，那么在第九行变为比较
# hold vs empty-prices[i]=hold + prices[i] - fee-price[i]=hold-fee<hold

