"""
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
方法1：动态规划 dp[i, j] = dp[i+1, j-1] and s[i]==s[j]
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ll = len(s)
        if ll <= 1: return s  # 长度小于等于2

        max_len = 0
        l, r = 0, 0

        dp = [[0 for i in range(ll)] for j in range(ll)]

        for i in range(ll):  # 为动规做准备
            dp[i][i] = 1
            if i >= 1:
                dp[i][i - 1] = (s[i] == s[i - 1])

        for i in range(ll - 2, -1, -1):  # 根据递推公式确定遍历的顺序
            for j in range(i + 1, ll):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and j - i > max_len:
                    l, r = i, j
                    max_len = j - i  # watch
        return s[l: 1 + r]

# ################################# 中心扩展 #######################################
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome2(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# ################################# 马拉车算法 #######################################
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2  # 返回臂长

    def longestPalindrome3(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]


"""
方法1：动态规划 时空复杂度都是O(N方)
方法2：中心扩展 时间复杂度N方，空间O(1)  
方法二注意要考虑两种情况：从中心1位扩展，从中心两位扩展(例如："cbbd"，回文中心位两位)
方法3：

优先：中心扩展
"""