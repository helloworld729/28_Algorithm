"""
题目：给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n
条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 
轴共同构成的容器可以容纳最多的水。
链接：https://leetcode-cn.com/problems/container-with-most-water
"""
class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        res = min(height[l], height[r]) * (r-l)
        while l < r:
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            res = max(res, min(height[l], height[r]) * (r - l))
        return res

    def maxArea2(self, height) -> int:
        l, r = 0, len(height) - 1
        res = min(height[l], height[r]) * (r-l)

        while l < r:
            if height[l] <= height[r]:
                temp = height[l]
                while l + 1 <= r and height[l] <= temp:
                    l += 1
            else:
                temp = height[r]
                while r-1 >= l and height[r] <= temp:
                    r -= 1
            res = max(res, min(height[l], height[r])*(r-l))

        return res

# 方法：直接双指针从两侧往中间运动，记录过程中的每一个面积
# 优化：在向内运动的时候，只有遇到比前值更大的值才有计算的
# 必要，因为宽度已经压缩，高度必须升高，面积才有可能大。


