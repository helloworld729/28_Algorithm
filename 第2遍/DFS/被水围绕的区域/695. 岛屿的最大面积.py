"""
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者
竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。) 

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

方法：每次遇到1就开始深搜，dfs的过程中染色，并且记录深搜的次数。
链接：https://leetcode-cn.com/problems/max-area-of-island
"""
class Solution:
    def maxAreaOfIsland1(self, grid) -> int:
        if not grid: return 0

        r, c = len(grid), len(grid[0])
        color = -1
        def dfs(i, j):
            grid[i][j] = color
            nums[-1] += 1

            for (m, n) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if 0<=m<=r-1 and 0<=n<=c-1 and grid[m][n]==1:
                    dfs(m, n)
        nums = [0]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    nums.append(0)
                    dfs(i, j)

        return max(nums)
    def maxAreaOfIsland2(self, grid) -> int:
        # 为什么不行呢
        if not grid: return 0

        r, c = len(grid), len(grid[0])
        color = -1

        dfs = []
        nums = [0]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    nums.append(0)
                    dfs.append((i, j))
                    while dfs:
                        p0, p1 = dfs.pop()
                        grid[p0, p1] = color
                        nums[-1] += 1
                        for (m, n) in [(p0, p1 - 1), (p0, p1 + 1), (p0 - 1, p1), (p0 + 1, p1)]:
                            if 0 <= m <= r - 1 and 0 <= n <= c - 1 and grid[m][n] == 1:
                                dfs.append((m, n))
        return max(nums)

