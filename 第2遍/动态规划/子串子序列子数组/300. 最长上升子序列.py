# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
class Solution:
    def lengthOfLIS(self, nums) -> int:
        ll  = len(nums)
        res = 1
        if ll < 2: return ll

        dp = [1] * ll
        for i in range(ll):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
                    res = max(res, dp[i])
        return res

    def lengthOfLIS2(self, nums) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                # 上升直接增加
                d.append(n)
            else:
                # 降低的话，bisect_insert_left
                l, r = 0, len(d)
                while l < r:
                    mid = l + (r-l) // 2
                    if d[mid] < n:
                        l = mid + 1
                    else: r = mid
                d[l] = n

        return len(d)

    def lengthOfLIS3(self, nums) -> int:
        import bisect
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                pos = bisect.bisect_left(d, n)
                d[pos] = n
        return len(d)

lst = [4, 10, 4, 3, 8, 9]
a = Solution()
print(a.lengthOfLIS2(lst))


# 方法1：dp[i] 以dp[i]结尾的最长上升序列的长度
# 方法二：贪心 + 二分 dp[i]长度为i的序列的当前最小结尾数字(贪心)



