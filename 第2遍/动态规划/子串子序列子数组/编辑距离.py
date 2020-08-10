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
D[i][j]:A的前i个字母和B的前j个字母之间的编辑距离
# 边界情况：与空串比较
dp[i][j] = min(
dp[i-1][j]        # 和线面的同理
dp[i][j-1]+1      假如已知和第二个单词前j-1长度的距离，那么在第一单词后面添加单词2的最后一个char即可|或者第二单词删除
dp[i-1][j-1]+1/0  对应修改操作，已知两单词都后退一步的距离，那么最后一个单词如果相同则距离不变，否则加一
虽然说，提供了三个上界，但是子问题包含了所有的可能，只要边界计算正确，一定有一个最小值。
)
"""

class Solution:
    def minDistance(self, word1, word2):
        # 用第一个单词构建行，第二个单词构建列
        l1, l2 = len(word1), len(word2)
        if not l1 * l2: return max(l1, l2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        # boundary process
        for i in range(l1+1): dp[i][0] = i
        for j in range(l2+1): dp[0][j] = j

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                first_add = dp[i-1][j] + 1
                first_del = dp[i][j-1] + 1
                k = 0 if word1[i-1] == word2[j-1] else 1
                first_change = dp[i-1][j-1] + k
                dp[i][j] = min(first_add, first_del, first_change)

        return dp[-1][-1]

# 状态转移==>选择有哪几个