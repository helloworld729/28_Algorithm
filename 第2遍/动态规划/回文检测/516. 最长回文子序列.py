"""
"bbbab"
输出:4 一个可能的最长回文子序列为 "bbbb"。
状态定义：dp[i, j]:在i-->j区间
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ll = len(s)
        if ll < 2: return ll
        dp = [[0 for _ in range(ll)] for _ in range(ll)]
        for i in range(ll):
            dp[i][i] = 1

        res = 1

        for i in range(ll - 2, -1, -1):
            for j in range(i + 1, ll):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])  # i+1不越界，那么i左边界为:ll-2
                res = max(res, dp[i][j])

        return res


# 如何快速定去区间，而不会越界?
# 先写一个框架，然后自底向上推断出左右区间。