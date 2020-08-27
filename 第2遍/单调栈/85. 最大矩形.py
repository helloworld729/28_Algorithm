class Solution:
    def maximalRectangle(self, matrix) -> int:
        """单调栈求柱状图最大矩形的方法"""
        def max_area(lst):
            lst = [0] + lst + [0]
            st = []  # 维护一个单调增的栈
            res = 0
            for i in range(len(lst)):
                while st and lst[st[-1]] > lst[i]:
                    index = st.pop()
                    h = lst[index]
                    w = i - st[-1] - 1  # 为什么不是i - index呢？
                    res = max(res, h * w)
                st.append(i)
            return res

        if matrix == [] or matrix == [[]]: return 0
        r, c = len(matrix), len(matrix[0])
        dp = [0 for _ in range(c)]
        res = 0
        for i in range(r):
            for j in range(c):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            res = max(res, max_area(dp))
        return res


"""
题目：给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
      https://leetcode-cn.com/problems/maximal-rectangle/
方法：首先定义一个求柱状图上最大矩形的办法，然后以每一行为底，求每一个position上连续
      1的个数，作为高度，然后逐层求最大矩形的面积。
关键：函数中矩形宽度的左边界计算 + 注意是连续1的高度。
左边界计算：有可能索引出现0,2,5现在弹出5宽度怎么算呢？因为是单调递增栈所以3,4,一定
            比5高，或者我们可以说:左边有索引的都是height比较低的，被干掉
规律：左边有索引的都是height比较低的，被干掉的都是比自己高的。
"""

