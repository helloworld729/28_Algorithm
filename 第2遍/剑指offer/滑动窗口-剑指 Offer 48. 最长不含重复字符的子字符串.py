class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1: return length

        pos_mem = {s[0]:0}
        dp = [1] * len(s)
        res = 0

        for i in range(1, length):
            if s[i] not in pos_mem:
                dp[i] = dp[i-1] + 1
            else:
                dis = i - pos_mem[s[i]]
                if dis <= dp[i-1]:
                    dp[i] = dis  # 新开
                else:
                    dp[i] = dp[i-1] + 1  # 增长
            # print(dp[i])
            pos_mem[s[i]] = i
            res = max(res, dp[i])
        return res


# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 解题过程：首先有以下定义：
# 1、字距j-i:同一字符在s的i和j位置，则字距为j-i
# 2、字长dp[i]:以字符s[i]结尾的最长无重复字符串长度
#
# 显然问题的关键在于，假如我们已知了dp[i-1]，如何求dp[i]呢？
# 进一步的，我们需要知道s[j]有没有出现在前一字符的字长范围内，
# 那么有两种情况：
# 1、已经被包含-->重新计算长度
# 2、没有被包含-->dp[i-1]即可
# 那么如何知道有没有出现过呢？-->哈希map，记录每个字符最新出现的位置。

