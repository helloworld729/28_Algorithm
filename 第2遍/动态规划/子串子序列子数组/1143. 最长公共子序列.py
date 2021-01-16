"""1143. 最长公共子序列"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 += "#"; text2 += "#"
        l1, l2 = len(text1), len(text2)
        res = 0
        # 以第一个单词为行坐标，第二个单词为列坐标
        dp = [[0 for i in range(l2)] for j in range(l1)]
        for i in range(l1-2, -1, -1):
            for j in range(l2-2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return res

"""
状态：dp[i][j]:到单词2的第i个位置，与第1个单词第j个位置最长的公共长度。
递推：
dp[i,j] = dp[i+1][j+1] + 1            # 相等
dp[i,j] = max(dp[i, j+1],dp[i+1, j])  # 不相等
返回：dp[-1][-1]

避免边界处理的trick：两个单词增加哨兵，然后for遍历的时候从位置1开始
如果把字符看做是list的话，那么添加到末尾的时间复杂最低为O(1)，所以
采用了这种方法，并且在遍历的时候倒序
"""