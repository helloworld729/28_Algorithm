# 题目：从左上到右下移动，棋盘上每个位置都有几个数字，每移动一次的得分是
# 移动前后棋盘数字差的绝对值，求最少得到多少分。

n = int(input())
grid = []
for i in range(n):
    data = list(map(int, input().split()))
    grid.append(data)
res = float("inf")
color = -1

def dfs(r, c, score):
    if r == c == n-1:
        global res
        res = min(res, score)
        return

    for (i, j) in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
        if 0 <= i and i <= n-1 and 0 <= j and j <= n-1 and grid[i][j] != color:
            origin_mem = grid[r][c]  # 记忆
            grid[r][c] = color       # 染色
            dfs(i, j, score + abs(origin_mem - grid[i][j]))  # 推进
            grid[r][c] = origin_mem  # 恢复

dfs(0, 0, 0)
print(grid)
print(res)