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

grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
]

# 思路 找到1后以此为根据地进行深度优先搜索
def deepsearch(grid, r, l, row, col):
    """
    坐标(r,l)为base，开始search，search的结果就是相连的1标记为0
    :param grid: 二维列表
    :return: 标记后的网格
    """
    grid[r][l] = 0
    for i, j in [(r-1, l), (r, l-1), (r, l+1), (r+1, l)]:
        if 0 <= i <= row-1 and 0 <= j <= col-1 and grid[i][j] == 1:
            deepsearch(grid, i, j, row, col)


def island_nums(grid):
    """注意两个函数小标的范围"""
    if not grid or not grid[0]:
        return 0
    row, col = len(grid), len(grid[0])
    count = 0
    for r in range(row):
        for l in range(col):
            if grid[r][l] == 1:
                count += 1
                deepsearch(grid, r, l, row, col)
    return count

# print(island_nums(grid))

def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按值(value)排序:")
    res = sorted(key_value.items(), key=lambda kv: kv[0])  # 返回键值对列表
    return res


def main():
    print(dictionairy())


if __name__ == "__main__":
    main()