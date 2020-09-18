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

        index = list()
        columns, left, right = set(), set(), set()
        dfs(columns, left, right, 0, index)  # 前三个是记录，下一步要确定的行
        return self.res

queen = Solution()
res = queen.solveNQueens(9)
print(res)


"""
很明显是dfs问题，问题是如何剪枝
最开始的思路是：行从上到下的过程中，对列进行搜索，然后将相关的行、列都染色
dfs推进之后，在把颜色还原。
每一个位置都有可能是或者不是皇后，复杂度为2的N方次。果断超时。

优化算法：
每一次确定列的位置，第一行有N种选择，第2行有N-1中选择，时间复杂度为N!
为了减少总的时间复杂度，希望尽快的确定当前的位置是不是在前置的行列或者
对角线的位置，必须寻找规律。
矩阵左下规律：行 + 列 相等
矩阵右下规律：列 - 行 相等
用hashset加速，注意set和dict类似，都是无序的，只可以用来判断列是否冲突
至于添加的顺序，我用index列表保证了。
"""


