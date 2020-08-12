"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
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
链接：https://leetcode-cn.com/problems/surrounded-regions
思路：dfs 第一遍变边界开始向内染色，第二遍将没有被染色的"O"改写成"X"
"""
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return board

        r, c = len(board), len(board[0])
        color = -1

        def dfs(i, j):
            board[i][j] = color
            for (m, n) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if 0<=m<=r-1 and 0<=n<=c-1 and board[m][n]=="O":
                    dfs(m, n)

        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r-1 or j == 0 or j == c-1) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == color:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"