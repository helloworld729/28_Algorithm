"""
我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：
如果 x 是偶数，那么 x = x / 2
如果 x 是奇数，那么 x = 3 * x + 1
比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。
给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，
如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。
请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。
注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。
输入：lo = 12, hi = 15, k = 2; 输出：13
解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
链接：https://leetcode-cn.com/problems/sort-integers-by-the-power-value
方法：直接递归太耗时，trick：递归+记忆
"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        back_dict = {1:0}

        def cal_weight(x):
            if x in back_dict:
                return back_dict[x]
            ans = 1 + cal_weight(x // 2) if x%2 == 0 else 1 + cal_weight(3 * x + 1)
            back_dict[x] = ans
            return ans

        weight_dict = {i:cal_weight(i) for i in range(lo, hi+1)}
        res = sorted(weight_dict.items(), key=lambda x:(x[1], x[0]))
        return res[k-1][0]
