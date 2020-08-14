"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于
k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 

输入：m = 2, n = 3, k = 1
输出：3

链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof

note：有些区域数值上满足要求，但是机器人不可达(因为每次只能在上下左右活动，但是可行域
实在不同的快)
"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if m * n == 0: return 0
        if k == 0: return 1

        color = 1
        grid = [[0 for i in range(n)] for j in range(m)]

        def pos_sum(num):
            res = 0
            while num > 0:
                rest = num % 10
                num = num // 10
                res += rest
            return res

        def dfs(i, j):
            grid[i][j] = color
            for (p, q) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= p <= m - 1 and 0 <= q <= n - 1 and pos_sum(p) + pos_sum(q) <= k and grid[p][q] != color:
                    dfs(p, q)

        dfs(0, 0)

        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] != color and pos_sum(r)+pos_sum(c) <= k:
        #             dfs(r, c)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
        return count