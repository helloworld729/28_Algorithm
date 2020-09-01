class Solution:
    def spiralOrder(self, matrix):
        pre2next  = {"right": "down", "down": "left", "left": "up", "up": "right"}
        pos_back  = {"right": [1, -1], "down": [-1, -1], "left": [-1, 1], "up": [1, 1]}
        pos_add   = {"right": [0,1], "down": [1,0], "left": [0, -1], "up": [-1, 0]}
        pre = "right"
        res = []
        i, j = 0, 0

        while 0 <= i <= len(matrix)-1 and 0<= j <= len(matrix[0])-1 and matrix[i][j] is not None:
            while 0 <= i <= len(matrix)-1 and 0<= j <= len(matrix[0])-1 and matrix[i][j] is not None:
                res.append(matrix[i][j])
                matrix[i][j] = None
                a, b = pos_add[pre]
                i, j = i + a, j + b
            a, b = pos_back[pre]
            i, j = i + a, j + b
            pre = pre2next[pre]

        return res

"""
列表类的题目中，判断语句不要用简写，否则可能会遇到数据0被判为False
而提前停止。
"""