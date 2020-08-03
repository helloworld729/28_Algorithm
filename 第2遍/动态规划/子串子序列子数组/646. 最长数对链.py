# 与435无重叠区间几乎一样
# 与452引爆气球一样
"""
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才
可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到
所有的数对，你可以以任何顺序选择其中的一些数对来构造。
输入: [[1,2], [2,3], [3,4]]
输出: 2
解释: 最长的数对链是 [1,2] -> [3,4]
链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
"""

class Solution:
    def findLongestChain1(self, pairs) -> int:
        """排序+DP"""
        ll = len(pairs)
        if ll < 2: return 0
        dp = [1] * ll
        max_len = 1

        pairs.sort(key=lambda x: x[1])

        for i in range(ll):
            for j in range(i-1, -1, -1):
                # 如果区间i的左边界>区间j的右边界，那么长度加1
                # 又因为排了序，前面不会有再长的上升区间长度，所以berak
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    max_len = max(max_len, dp[i])
        return max_len

    def findLongestChain2(self, pairs) -> int:
        """利用排序对，DP优化"""
        ll = len(pairs)
        if ll < 2: return 0
        dp = [1] * ll
        max_len = 1

        pairs.sort(key=lambda x: x[1])

        for i in range(ll):
            for j in range(i-1, -1, -1):
                # 如果区间i的左边界>区间j的右边界，那么长度加1
                # 又因为排了序，前面不会有再长的上升区间长度，所以berak
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
            dp[i] = max(dp[i], dp[i-1])
            max_len = max(max_len, dp[i])

        return max_len

    def findLongestChain3(self, pairs) -> int:
        """按照第二元素排序后，贪心"""
        if len(pairs) < 2: return len(pairs)
        cur = float("-inf")
        res = 0
        for l, r in sorted(pairs, key = lambda x: x[1]):
            if cur < l:
                cur = r
                res += 1
        return res