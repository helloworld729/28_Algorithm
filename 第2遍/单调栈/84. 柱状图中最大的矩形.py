class Solution:
    def largestRectangleArea(self, heights) -> int:
        st = []
        res = 0
        ll = len(heights)
        for i in range(ll):
            if st and heights[st[-1]] > heights[i]:
                while st and heights[st[-1]] > heights[i]:
                    index = st.pop()
                    h = heights[index]
                    w = i - st[-1]-1 if st else i
                    res = max(res, h*w)
            st.append(i)

        for i in range(len(st)):
            if i == 0:
                w = st[-1]+1
            else:
                w = st[-1] - st[i-1]
            res = max(res, heights[st[i]]*w)  # 高度*宽度
        return res

    def largestRectangleArea2(self, heights) -> int:
        heights = [0] + heights + [0]
        st = [0]
        res = 0
        ll = len(heights)
        for i in range(1, ll):
            if st and heights[st[-1]] > heights[i]:
                while st and heights[st[-1]] > heights[i]:
                    index = st.pop()
                    h = heights[index]
                    w = i - st[-1]-1  # 保证栈非空
                    res = max(res, h*w)
            st.append(i)
        return res

height = [2,1,5,6,2,3]
a = Solution()
print(a.largestRectangleArea(height))


"""
方法1要考虑两种边界：空栈、遍历完成后栈非空(单调升)
使用方法2，可以免去边界判断，很帅的方法

宽度计算：以 4 2 0 3 2 5为例，不要用固定值计算延伸宽度，而是动态的值(i-1,而不是0这种)
"""
