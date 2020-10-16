from typing import List
class Solution:
    def __init__(self):
        self.res = 0

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        ll = len(nums)
        dp = [[0 for _ in range(ll)] for _ in range(ll)]
        for i in range(ll-1, -1, -1):  # 由于内部计算的是开区间，所以这里都要到边界
            for j in range(i+1, ll):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        return dp[0][ll-1]

    def maxCoins2(self, nums: List[int]) -> int:
        def dfs_search(cans, value):
            """候选路径，已有的价值"""
            ll = len(cans)
            if ll == 2:
                self.res = max(self.res, value)
                return

            for i in range(1, ll-1):
                new_value = cans[i-1] * cans[i] * cans[i+1]
                value += new_value
                dfs_search(cans[:i]+cans[1+i:], value)
                value -= new_value

        dfs_search([1]+nums+[1], 0)
        return self.res

lst = [3,1,5,8]
a = Solution()
print(a.maxCoins2(lst))


"""
思路：动态规划 dp[i][j]：打破区间(i, j)开区间能够获得的分数
      dp[i][j] = max(dp[i][k] + dp[k][j] + p[i][k][j])
      假设横坐标为j，纵坐标为k，那么：
      [i][k]为二维矩阵左边部分，[k][j]为下边部分
      
      时间复杂度O(N3)；空间复杂度为O(N2)
      
方法2：dfs 超时，哪里有重复计算呢？

"""