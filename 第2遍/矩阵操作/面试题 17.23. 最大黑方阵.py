from collections import defaultdict
class Solution:
    def findSquare(self, matrix):
        if not matrix: return []
        mxrow = defaultdict(int)  # 向右的臂长
        mxcol = defaultdict(int)  # 向下的臂长
        rows, cols = len(matrix), len(matrix[0])
        res = []
        # 遍历行
        for r in range(rows)[::-1]:
            # 遍历列
            for c in range(cols)[::-1]:
                if matrix[r][c] == 0:
                    mxrow[r, c] = 1 + mxrow[r, c + 1]  # 右行
                    mxcol[r, c] = 1 + mxcol[r + 1, c]  # 下列

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mxsize = min(mxrow[r, c], mxcol[r, c])  # 取臂长最小值作为最大值
                    cursize = 0 if not res else res[2]      # 已知的最大边长
                    for size in range(mxsize, cursize, -1):
                        # 右定点向下的臂长，
                        if mxcol[r, c + size - 1] >= size and mxrow[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res


a = Solution()
lst = [
   [0,0,0],
   [0,1,0],
   [0,0,0]
]
print(a.findSquare(lst))

# 用动态规划，先统计每个节点的右臂长和下臂长
# 最重要的一点：这个题不要求内部全为1，而是只要计算变长
