"""
1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符
的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个
字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

思路：转移公式
dp[i,j] = dp[i+1][j+1]  # 相等
dp[i,j] = max(dp[i, j+1],dp[i+1, j])  # 不相等
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        if not l1*l2: return 0
        dp = [[0 for i in range(l1+1)] for j in range(l2+1)]  # 以单词1为列，单词2为行
        for i in range(l2-1, -1, -1):
            for j in range(l1-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]