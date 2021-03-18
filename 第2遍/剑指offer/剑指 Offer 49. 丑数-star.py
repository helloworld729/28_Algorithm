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

    def nthUglyNumber2(self, n: int) -> int:
        dp = [1] * n
        two, three, five = 0, 0, 0
        for i in range(1, n):
            candidate = min(2 * dp[two], 3 * dp[three], 5 * dp[five])
            if candidate == 2 * dp[two]:
                two += 1
            elif candidate == 3 * dp[three]:
                three += 1
            elif candidate == 5 * dp[five]:
                five += 1
            dp[i] = candidate
        return dp[-1]

print(Solution().nthUglyNumber(10))
print(Solution().nthUglyNumber2(10))

"""
把一个丑数乘以2、3、5后肯定还是丑数，所以定义3个指针
分别用于乘已经存在的丑数，那么就可以生成所有的丑数

1、a, b, c是三个指针，表示把当前值乘以2或者3或者5
2、每次就有3个候选值，选择最小的作为命中值
3、对应的指针后移一位

方法2的错误就是使用了elif，但是应该是用并列的if。因为：two指针指向丑数3的时候
three指针也一定指向丑数2[假如three指向1，那么two会等待，如果three指向3，说明9已经生成，two不可能指向3]，
所以，这个时候两个指针都应该后移，否则会生成两个6
"""