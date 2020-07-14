"""
200. 岛屿数量<br>
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。可以把岛屿看做集中连片的1。
示例 1:
输入:
1 1 1 1 0<br>
1 1 0 1 0<br>
1 1 0 0 0<br>
0 0 0 0 0<br>
输出: 1<br>
"""

################################# 方法1深度优先搜索 ########################################
# def dfs(grid, r, c):
#     grid[r][c] = 0  # 记忆搜索将格点标记位0
#     nr, nc = len(grid), len(grid[0])
#     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右
#         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
#             dfs(grid, x, y)
# def numIslands(grid) -> int:
#     nr = len(grid)
#     if nr == 0:
#         return 0
#     nc = len(grid[0])
#     num_islands = 0
#     for r in range(nr):
#         for c in range(nc):
#             if grid[r][c] == 1:  # 只要出现了1，必定对应一个岛屿
#                 num_islands += 1
#                 dfs(grid, r, c)
#     return num_islands

grid = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
       ]

# print(numIslands(grid))

def island_nums(grid) -> int:
    def dfs(grid, i, j):
        for (r, c) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = 0
                print("here")
                dfs(grid, r, c)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = 0
                count += 1
                dfs(grid, i, j)
    return count

print(island_nums(grid))
