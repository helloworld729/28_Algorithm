"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面
的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行
第二个格子之后，路径不能再次进入这个格子。
示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
思路：dfs+染色，但是不用重新开批空间，直接在原数组上染色即可
"""
class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])  # 1, 2
        def dfs(i, j, index):
            # 进来就染色，如果没有命中就重新染回来
            temp = board[i][j]
            board[i][j] = "/"
            if index == len(word)-1: return True
            for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[index+1]:
                    if dfs(ni, nj, index+1):
                        return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):  # 已经完成匹配的单词索引
                        return True
        return False

