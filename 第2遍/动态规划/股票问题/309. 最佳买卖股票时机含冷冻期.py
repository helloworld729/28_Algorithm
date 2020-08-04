class Solution:
    def maxProfit(self, prices) -> int:
        """比手续费 增加一个状态"""
        ll = len(prices)
        if ll < 2: return 0
        empty, frozen, hold = 0, 0, 0
        for i in range(1, ll):
            new_hold = prices[i]-prices[i-1] + hold
            empty_back = empty
            empty = max(empty,  frozen)  # right
            frozen = new_hold
            hold =  max(empty_back,  new_hold)      # right
        return max(empty, frozen)