"""1143. 最长公共子序列"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = "#" + text1
        text2 = "#" + text2
        l1, l2 = len(text1), len(text2)
        dp = [[0 for i in range(l1)] for j in range(l2)]
        # 第一个单词为列，第二个单词为行
        for i in range(1, l2):      # 第2个单词的位置
            for j in range(1, l1):  # 第1个单词的位置
                # 基础当量
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                # 加成
                if text2[i] == text1[j]:  # 参照for循环定出此处的index与单词匹配关系
                    dp[i][j] = 1 + dp[i-1][j-1]
        return dp[-1][-1]

"""
状态：dp[i][j]:到单词2的第i个位置，与第1个单词第j个位置最长的公共长度。
递推：
dp[i,j] = dp[i+1][j+1] + 1            # 相等
dp[i,j] = max(dp[i, j+1],dp[i+1, j])  # 不相等
返回：dp[-1][-1]

避免边界处理的trick：两个单词增加前导符，然后for遍历的时候从位置1开始
"""