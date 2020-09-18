class Solution:
    def getMaxMatrix(self, matrix):
        def max_area(heights, baseline):
            # 最大子序和
            heights  = [0] + heights
            baseline = float("-inf")
            l_back = r = l = 0
            for i in range(1, len(heights)):
                if heights[i-1] > 0:
                    heights[i] = heights[i] + heights[i - 1]
                else:
                    l = i  # 新的左边界,新的左边界不一定带来最大的面积
                    # 只有得到的面积大于baseline，才会统一的更新返回的边界
                if heights[i] > baseline:
                    baseline = heights[i]
                    r = i  # 新的有边界
                    l_back = l
            return baseline, l_back-1, r-1  # 和添加哨兵之前对齐

        ll = len(matrix)
        baseline = float("-inf")
        res = []
        for up in range(ll):  # 闭区间
            heights = [0] * len(matrix[0])  # columns
            for down in range(up, ll):
                for i in range(len(matrix[0])):
                    heights[i] += matrix[down][i]
                sub_sum, l, r = max_area(heights, baseline)
                if sub_sum > baseline:
                    baseline = sub_sum
                    # print(sub_sum, up, l, down, r)
                    res = [up, l, down, r]
        return res

a = Solution()
matrix = [[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]
print(a.getMaxMatrix(matrix))

# 时间复杂度：O(N方M)
# 考察最大子序和，注意在就不同矩阵区间的高度heights，用累加的方式
# 每次叠加上最新的一行即可，不必重复计算。  # 否则超时

