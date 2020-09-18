class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = temp

    def rotate2(self, matrix):
        # 思路： 转置 + 翻转
        # 首先，转置
        rows = len(matrix)
        for i in range(rows):
            for j in range(i, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 每一行都反转
        for i in range(rows):
            matrix[i].reverse()

