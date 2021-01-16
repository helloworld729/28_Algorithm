# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
class Solution:
    def lengthOfLIS(self, nums) -> int:
        # dp[i]表示到当前位置的最大上升序列长度
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
        d = []  # 目标上升序列
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

lst = [1, 3, 4, 2, 6, 10]
a = Solution()
print(a.lengthOfLIS3(lst))

# 方法1：dp[i] 以dp[i]结尾的最长上升序列的长度
# 方法二：贪心 + 二分 dp[i]长度为i的序列的当前最小结尾数字(贪心)
# 理解方法2的关键是 d数组数多个排序结构的融合，例如：数组为[1,3,4,2,6]
# 那么第一个上升序列是 [1,3,4]，当遇到2的时候，将2替换掉3 这个操作
# 既没有影响原先序列的长度和末尾元素，而且又开始了第二个上升序列

