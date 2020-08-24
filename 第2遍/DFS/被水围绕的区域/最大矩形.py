class Solution:
    def maximalRectangle(self, matrix) -> int:
        r, c = len(matrix), len(matrix[0])
        element = [[0, 0], 0, 0]  # 对角的长度和宽度、横条的长度、竖条的长度
        dp = [[ [[0, 0], 0, 0] for i in range(c + 1)] for j in range(r + 1)]
        res = 0

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j][1] = 1 + dp[i][j - 1][1]  # 横条
                    dp[i][j][2] = 1 + dp[i - 1][j][2]  # 竖条
                    c_l = min(dp[i - 1][j - 1][0][0], dp[i][j - 1][1]) + 1
                    c_w = min(dp[i - 1][j - 1][0][1], dp[i - 1][j][2]) + 1
                    dp[i][j][0] = [c_l, c_w]
                    res = max(res, dp[i][j][1], dp[i][j][2], c_l * c_w)

        return res

matrix = [
  ["1","1","1","1"],
  ["1","1","1","1"],
  ["1","1","1","1"],
]

a = Solution()
print(a.maximalRectangle(matrix))