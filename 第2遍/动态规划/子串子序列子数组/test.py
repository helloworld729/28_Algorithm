class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = "#" + word1, "#" + word2
        l1, l2 = len(word1), len(word2)
        # 单词1为列，单词2为行
        dp = [[0 for i in range(l1)] for j in range(l2)]
        for i in range(l1): dp[0][i] = i
        for j in range(l2): dp[j][0] = j

        # i为行，表示单词2的pos
        for i in range(1, l2):
            # j为列，表示单词1的pos
            for j in range(1, l1):
                temp = 0 if word2[i] == word1[j] else 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + temp)
        return dp[-1][-1]


a = Solution()
s1 = "horse"
s2 = "ros"
print(a.minDistance(s1, s2))

# 为什么添加前导符呢？为了使index与实际感觉一致

