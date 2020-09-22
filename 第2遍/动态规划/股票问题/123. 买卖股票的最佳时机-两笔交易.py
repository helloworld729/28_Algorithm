"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii

当优化空间的时候，为了避免定义临时变量，一定要注意倒着动规
"""
class Solution:
    def maxProfit(self, prices) -> int:
        ll = len(prices)
        if ll <2: return 0
        if ll == 2: return max(0, prices[1]-prices[0])
        one_in, res = 0, float("-inf")
        one_out = two_in = two_out = float("-inf")

        for i in range(1, ll):
            increase = prices[i]-prices[i-1]
            two_out = max(two_in + increase, two_out)
            two_in  = max(two_in + increase, one_out)
            one_out = max(one_in + increase, one_out)
            one_in  = max(one_in + increase, 0)  # 第一项表示前面已经购买，只是维持，第二项表示真的第一次购买

            res = max(res, one_out, two_out)
        return max(0, res)

    def maxProfit2(self, prices) -> int:
        ll = len(prices)
        if ll <2: return 0
        if ll == 2: return max(0, prices[1]-prices[0])
        one_in, res = -prices[0], float("-inf")
        one_out = two_in = two_out = float("-inf")

        for i in range(1, ll):
            two_out = max(two_in + prices[i], two_out)
            two_in  = max(two_in, one_out - prices[i])
            one_out = max(one_in + prices[i], one_out)
            one_in  = max(one_in, -prices[i])  # 第一项表示前面已经购买，只是维持，第二项表示真的第一次购买
        res = max(res, one_out, two_out)
        return max(0, res)


a = Solution()
lst = [3, 3, 5, 3]
print(a.maxProfit2(lst))


# 方法1：价值包括两部分：手里面的前 + 金子的价值
# 方法2：价值包含一部分：手里面的钱
