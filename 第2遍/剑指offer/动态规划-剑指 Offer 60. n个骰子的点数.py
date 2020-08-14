"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。 
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
方法：动态规划dp[i][j]:前i个骰子，和为j的组合数最后统一除以6的n次方
"""

class Solution:
    def twoSum(self, n: int):
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]

        for i in range(1, 6 + 1):
            dp[1][i] = 1

        for i in range(2, n + 1):
            # 可以考虑在这个地方增加一个窗口和，
            for j in range(i, 6 * i + 1):
                for k in range(1, 6 + 1):  # 分别对用本次扔1-6点
                    if j - k >= i-1:  # 严格意义上来讲，下界是i-1，但是二维的时候可以松弛为1，因为多加的部分也是0
                        dp[i][j] += dp[i - 1][j - k]

        res = []
        for d in dp[-1][n:]:
            probility = d / pow(6, n)
            res.append(probility)
        return res

    def twoSum2(self, n: int):
        """优化空间复杂度"""
        dp = [0 for _ in range(6*n+1)]
        for i in range(1, 6+1):
            dp[i] = 1

        for i in range(2, n+1):
            for j in range(6*i, i-1, -1):
                dp[j] = 0  # watch
                for k in range(1, 6+1):  # 分别对用本次扔1-6点
                    if j-k >= i-1:  # 严格下界
                        dp[j] += dp[j-k]
        res = []
        for d in dp[n:]:
            probility = d/pow(6, n)
            res.append(probility)

        return res

# 哈额可以继续优化时间，应为每次向前扫描很多部分重叠