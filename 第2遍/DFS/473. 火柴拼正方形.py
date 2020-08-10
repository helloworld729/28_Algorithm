"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

输入: [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。
链接：https://leetcode-cn.com/problems/matchsticks-to-square
dfs遍历
"""
class Solution:
    def makesquare(self, nums) -> bool:
        ll = len(nums)
        if ll < 4: return False
        total = sum(nums)
        sides = [0 for _ in range(4)]
        side_len = total // 4
        if side_len*4 != total: return False
        nums.sort(reverse=True)  # 先排序？假如有一个数比较大，能早停

        def dfs(index):
            if index == ll:
                return sides[0] == sides[1] == sides[2] == sides[3] == side_len

            for i in range(4):
                if nums[index] + sides[i] <= side_len:
                    sides[i] += nums[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= nums[index]

            return False
        return dfs(0)