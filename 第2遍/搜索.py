# ###################### 130. 被围绕的区域 ########################################
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
思路:从边界开始考虑，向内部搜索
"""
def solve(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    r, c = len(board), len(board[0])
    def dfs(board, i, j):
        for (h, l) in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
            if 0 <= h < r and 0 <= l < c and board[h][l] == "O":
                board[h][l] = "k"
                dfs(board, h, l)
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                if board[i][j] == "O":
                    board[i][j] = "k"
                    dfs(board, i, j)
    for i in range(r):
        for j in range(c):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "k":
                board[i][j] = "O"
# board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
# print(solve(board))
# print(board)
# [['X', 'O', 'X', 'O', 'X', 'O'],
#  ['O', 'X', 'X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X', 'X', 'O'],
#  ['O', 'X', 'O', 'X', 'O', 'X']]


# ########################## 200. 岛屿数量 ########################################
"""
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

def dfs(grid, r, c):
    grid[r][c] = 0  # 记忆搜索将格点标记位0
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右
        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
            dfs(grid, x, y)
def numIslands(grid) -> int:
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    num_islands = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == 1:  # 只要出现了1，必定对应一个岛屿
                num_islands += 1
                dfs(grid, r, c)
    return num_islands

# grid = [
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 1],
# ]
# print(numIslands(grid))

# ##################### 1391有效路径 ##################################################
"""
给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：

1 表示连接左单元格和右单元格的街道。
2 表示连接上单元格和下单元格的街道。
3 表示连接左单元格和下单元格的街道。
4 表示连接右单元格和下单元格的街道。
5 表示连接左单元格和上单元格的街道。
6 表示连接右单元格和上单元格的街道。


你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、
一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。

如果网格中存在有效的路径，则返回 true，否则返回 false 。
示例 1：
输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
链接：https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid
"""
def hasValidPath(grid) -> bool:
    r, c = len(grid), len(grid[0])
    match_back = {
        1: [[], [], [1, 4, 6], [1, 3, 5]],
        2: [[2, 3, 4], [2, 5, 6], [], []],
        3: [[], [2, 5, 6], [1, 4], []],
        4: [[], [2, 5, 6], [], [1, 3, 5]],
        5: [[2, 3, 4], [], [1, 4, 6], []],
        6: [[2, 3, 4], [], [], [1, 3, 5]],
    }
    def match(currp, nextp, curr_mem):
        (i, j), (h, l) = currp, nextp
        flag = False
        next_pos  = grid[h][l]
        if   h < i and next_pos in match_back[curr_mem][0]:
            flag = True
        elif h > i and next_pos in match_back[curr_mem][1]:
            flag = True
        elif l < j and next_pos in match_back[curr_mem][2]:
            flag = True
        elif l > j and next_pos in match_back[curr_mem][3]:
            flag = True
        return flag

    def dfs(grid, i, j):
        curr_mem = grid[i][j]
        for (h, l) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            curr_p, nextp = (i, j), (h, l)
            if 0 <= h < r and 0 <= l < c and grid[h][l] != -1 and match(curr_p, nextp, curr_mem):
                # 何时标记呢？当前点的表标记如果放在dfs之后的话会导致无限递归，所以在之前
                # 注意要设置mem，否则因为下一个候选位置在match的时候会报keyError
                grid[i][j] = -1
                dfs(grid, h, l)
                grid[h][l] = -1

    dfs(grid, 0, 0)
    print(grid)
    if c <= 1:
        return True

    if grid[-1][-1] == -1:
        return True
    else:
        return False
grid = [[6,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [4,1,1,1,1,1,1,1,1,1,1,1,1,5],
        [6,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [4,1,1,1,1,1,1,1,1,1,1,1,1,5],
        [6,1,1,1,1,1,1,1,1,1,1,1,1,3],]
print(hasValidPath(grid))


