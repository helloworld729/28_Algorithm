# 输出所有从左上到右下的路径

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

color = 0
m = len(grid) - 1
n = len(grid[0]) - 1

def back(r, c):
    # r, c表示已经探索过的节点，因为到目前为止
    # 第24行，应该是那样的格式，即ij探索过了
    if (r + c) == (m + n):
        return [[]]  # 不能写成空，否则进不了上层的循环
    res = []
    for (i, j) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= i <= m and 0 <= j <= n and grid[i][j] != color:
            origin_mem = grid[i][j]  # 记忆
            grid[i][j] = color  # 染色
            for cans in back(i, j):
                res.append([(i, j)] + cans)
            grid[i][j] = origin_mem  # 恢复
    return res

#########################################################################
import time
start = time.time()
for i in range(100):
    origin_mem = grid[0][0]
    grid[0][0] = color
    result = back(0, 0)
    grid[0][0] = origin_mem
    for i in range(len(result)):
        result[i] = [(0, 0)] + result[i]
    result.sort(key=lambda x: len(x))
    for path in result:
        for (r, c) in path:
            print(grid[r][c], end=" ")
        print()
end = time.time()
print("耗时：", end - start)
# 耗时： 0.022001266479492188

