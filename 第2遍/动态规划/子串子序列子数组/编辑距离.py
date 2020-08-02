# ##################### 72. 编辑距离 ########################
"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
输入：word1 = "horse", word2 = "ros"
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

# 边界情况：与空串比较
"""

class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]  # 第一个单词构建行

        # 边界状态初始化
        for i in range(n + 1):  # 第0列初始化为行号
            D[i][0] = i
        for j in range(m + 1):  # 第0行初始化为列号
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):  # 第一个单词 行
            for j in range(1, m + 1):  # 第二个单词 列
                left = D[i - 1][j] + 1  # 删除第二个单词
                down = D[i][j - 1] + 1  #
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]

# 状态转移==>选择有哪几个