class Solution:
    def largestRectangleArea(self, heights) -> int:
        st = []  # 单调栈
        res = 0  #　最大值
        ll = len(heights)
        for i in range(ll):
            if st and heights[st[-1]] > heights[i]:  # 遇到比自己小的
                while st and heights[st[-1]] > heights[i]:  # 直到弹成单调栈
                    index = st.pop()
                    h = heights[index]
                    w = i - st[-1]-1 if st else i  # 索引在st[-1]到i之间都是长度比heights[index]要高的
                                                   # 如果栈为空的话说明整个左边都比当前index要高。
                    res = max(res, h*w)
            st.append(i)

        for i in range(len(st)):  # 假如最后栈没有空的话
            if i == 0:
                w = ll  # 整个数组最低值
            else:
                w = (ll-1) - st[i-1]  # 右边界-左边界
            res = max(res, heights[st[i]]*w)  # 高度*宽度
        return res

    def largestRectangleArea2(self, heights) -> int:
        heights = [0] + heights + [0]
        st = [0]
        res = 0
        for i in range(len(heights)):
            if st and heights[i] < heights[st[-1]]:
                while st and heights[i] < heights[st[-1]]:
                    index = st.pop()
                    h = heights[index]
                    w = i - st[-1] - 1
                    res = max(res, h*w)
            st.append(i)
        return res

height = [2,1,5,6,2,3]
a = Solution()
print(a.largestRectangleArea(height))


"""
题目来源：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

方法1要考虑两种边界：空栈、遍历完成后栈非空(单调升)
使用方法2：添加哨兵 免去边界判断，很帅的方法

方法1
宽度计算：以 4 2 0 3 2 5为例，不要用固定值计算延伸宽度，而是动态的值(i-1,而不是0这种)
特点：一遍遍历后，单调栈的第一个元素是整个heights最低的值，无论最后一个元素多大，都是
      栈的最后一个元素。也就是说遍历完成后栈保存的是介于最低值和右边界值之间的数据
"""
