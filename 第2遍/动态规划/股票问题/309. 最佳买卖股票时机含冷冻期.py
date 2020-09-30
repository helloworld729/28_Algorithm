class Solution:
    def maxProfit(self, prices) -> int:
        ll = len(prices)
        if ll < 2: return 0
        empty, frozen, hold = 0, float("-inf"), -prices[0]
        for i in range(1, ll):
            temp = frozen
            frozen = hold + prices[i]  # 卖掉持有
            hold = max(hold, empty-prices[i])
            empty = max(empty, temp)
        return max(empty, frozen)


# 持仓 <-- 持仓、空仓
# 空仓 <-- 空仓、冷冻
# 冷冻 <-- 持仓
# 持仓只能来自：持仓、空仓
# 冷冻只能来自于：持仓，换句话说冷冻不能自己传递到自己
# hold->frozen-empty-hold # 必须借助temp

