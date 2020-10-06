class Solution:
    def numberOfArithmeticSlices1(self, A) -> int:
        """公式计算法"""
        A += [float("inf")]
        ll = len(A)
        res = count = 0
        if ll < 3: return 0
        for i in range(2, ll):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
            else:
                res += count * (count+1) // 2
                count = 0
        return res

    def numberOfArithmeticSlices2(self, A) -> int:
        """dp法"""
        n = len(A)
        if n < 3: return 0
        dp = [0 for _ in range(n)]
        sum_ans = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                sum_ans += dp[i]
        return sum_ans


if __name__ == '__main__':
    a = Solution()
    lst = [1, 2, 3, 4, 5]
    print(a.numberOfArithmeticSlices1(lst))

"""
时间复杂度：O(N)
空间复杂度：O(N)
计算方法：以[1，2，3，4]为例子，首先求相邻两个数之间的差diffs:[1，1，1]
用双指针遍历diffs，直到两个指针的值不一样，此时temp_l记录的是该公差满足的区间
例如[1，1，1]长度为3，则最长等差数列长度为4，子区间的个数为 3 = 3 * 2 // 2
长度为3的：temp_l +1-3+1
长度为4的：temp_l +1-4+1
"""
