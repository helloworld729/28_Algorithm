"""
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

方法1：动态规划 dp[i, j] = dp[i+1, j-1] and s[i]==s[j]
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ll = len(s)
        if ll < 2: return s
        dp = [[0 for _ in range(ll)] for _ in range(ll)]
        for i in range(ll): dp[i][i] = True
        l = r = 0

        for i in range(ll - 2, -1, -1):
            for j in range(i, ll):
                if j == i + 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        dp[i][j] = True
                if dp[i][j] and j - i > r - l:
                    l, r = i, j

        return s[l: r + 1]