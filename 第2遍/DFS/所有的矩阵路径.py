# 输出所有从左上到右下的路径

# grid = [
#     [11, 12, 13, 14],
#     [15, 16, 17, 18],
#     [19, 20, 21, 22],
#     [23, 24, 25, 26]
# ]
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
color = 0; result = []
m, n = len(grid) - 1, len(grid[0]) - 1

def dfs(path):  # 栈尾是要探索的pos
    (r, c) = path[-1]
    if r + c == m + n:
        result.append(list(path))
        return
    if grid[r][c] != color:
        origin_mem = grid[r][c]  # 记忆
        grid[r][c] = color       # 染色
        for (i, j) in [(r+1, c), (r-1, c), (r ,c+1), (r, c-1)]:
            if 0 <= i <= m and 0 <= j <= n:
                path.append((i, j))
                dfs(path)  # 推进
                path.pop()
        grid[r][c] = origin_mem  # 恢复

import time
start = time.time()
for i in range(100):
    dfs([(0, 0)])
    result.sort(key=lambda x: len(x))
    for p in result:
        for (r, c) in p:
            print(grid[r][c], end="-")
        print()
end = time.time()
print("耗时：", end - start)

# dfs耗时 ： 0.637
# 回溯耗时： 0.022
# 可能是应为dfs的过程中，参数是一整个路径，
# 而回溯只需要是一个坐标，不过回溯的话，return
# 的也是一个大矩阵


