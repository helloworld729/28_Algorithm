class Solution:
    def __init__(self):
        self.flag = True

    def pathWithObstacles(self, obstacleGrid):
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        if not r*c: return []
        if obstacleGrid[0][0] == 1: return []
        res = [[]]

        def dfs(i, j, path):  # 新的起点， 已有的路径
            if path and [r-1, c-1] == path[-1]:
                res.append(list(path))
                self.flag = False
                return
            if self.flag:
                for (m, n) in [(i, 1+j), (i+1, j)]:
                    if 0 <= m and m <= r-1 and 0 <= n and n <= c-1 and obstacleGrid[m][n] == 0:
                        obstacleGrid[m][n] = 1
                        path.append([m, n])
                        dfs(m, n, path)
                        path.pop()
                        obstacleGrid[m][n] = 0

        dfs(0, 0, [[0, 0]])
        return res[-1]

grid = [
[0,0,0,0,0],
[0,0,0,0,1],
[0,0,0,1,0],
[0,0,0,0,0],
]
a = Solution()
print(a.pathWithObstacles(grid))


