class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0  # 三个指针
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5  # 3个候选值
            dp[i] = min(n2, n3, n5)  # 为了保证顺序，每次选择最小的
            if dp[i] == n2: a += 1   # 被命中的指针失效、后移
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]


"""
1、指针就是一个权重，能够生成被指向数乘以该权重的值
2、三个指针、每一步都有三个候选值，最小的使我们需要的
3、指针生效后后移。
"""