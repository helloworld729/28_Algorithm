class Solution:
    def __init__(self):
        self.res = []
    def solveNQueens(self, n: int):
        def gene_board(columns):
            answer = []
            for c in columns:
                temp = ["."] * n
                temp[c] = "Q"
                temp = "".join(temp)
                answer.append(temp)
            self.res.append(answer)

        def dfs(columns, left, right, row, index):
            if row == n:
                gene_board(index)
                return

            for i in range(n):
                if i in columns or i + row in left or i - row in right:
                    continue
                columns.add(i)      # 将皇后放在第i列
                index.append(i)     # 列放到index中
                left.add(i + row)   # 所有左下的共同点是 行 + 列 相等
                right.add(i - row)  # 所有右下的共同点是 列 - 行 相等
                dfs(columns, left, right, row+1, index)
                columns.remove(i)
                left.remove(i + row)
                right.remove(i - row)
                index.pop()

        columns, left, right = set(), set(), set()
        dfs(columns, left, right, 0, [])  # 前三个是记录，下一步要确定的行
        return self.res

queen = Solution()
res = queen.solveNQueens(9)
print(res)


