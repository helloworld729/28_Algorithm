"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达
棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
思路：动态规划，从邻居取一个最大值，加上自身
"""

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid
        for i in range(1, n):
            dp[0][i] = dp[0][i] + dp[0][i-1]
        for j in range(1, m):
            dp[j][0] = dp[j][0] + dp[j-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]