class Solution:
    def trap(self, height) -> int:
        height = height
        st = []
        res = 0
        ll = len(height)
        for i in range(ll):
            if st and height[st[-1]] < height[i]:  # 遇到非单调情况
                while st and height[st[-1]] < height[i]:
                    index = st.pop()
                    if st:
                        w = i - st[-1] -1
                        h = min(height[i], height[st[-1]]) - height[index]
                        res += w*h
            st.append(i)
        return res

    def trap2(self, height) -> int:
        res = 0
        ll = len(height)
        left = [height[0] for _ in range(ll)]
        right = [height[-1] for _ in range(ll)]
        for i in range(1, ll):
            left[i] = max(left[i-1], height[i])
            right[ll-1-i] = max(right[ll-i], height[ll-1-i])
        for i in range(ll):
            res += min(left[i], right[i]) - height[i]
        return res

    def trap3(self, height) -> int:
        ll = len(height)
        left, right = 0, ll-1
        left_max, right_max = float("-inf"), float("-inf")
        res = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:  # 左侧节点的左边最大高度是确定的，右边多大没关系，只要比left-max大就行
                res += left_max - height[left]
                left += 1
            else:  # 右侧节点的right-max是确定的，左边最大是多少没关系，只要比右边大就行
                res += right_max - height[right]
                right -= 1
        return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = Solution()
print(a.trap2(height))

"""
分析：维护一个单调递减栈，遇到比自己高的说明右边界可以确定，然后向左定出边界
      关键是高度界定，雨水的累计也是按照层次加的，而不是纵向。
     由于每个高度值最多入栈出栈各一次，所以时间复杂度为O(n)
      
方法2：动规的求处每个位置左边最大值、右边最大值，然后累加
方法3：双指针解法：两个指针分别从两侧向中间移动，较小的一端可以确定存水。
       在2中我们先确定每个位置的两侧边界，然后逐个求出可能存储的水量
       实际上可以利用单侧的值计算，假如右边界的值比左边界要大，那么就可以确定左指针能存多少水了
       反之，可以计算右指针的值。
"""
