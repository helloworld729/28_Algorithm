from typing import List

class Solution:
    def dailyTemperatures(self, T):
        # 思路：单调递减的栈，遇到比栈尾大的数，说明栈中的边界得以确定
        st = []
        ll = len(T)
        delay = [0 for _ in range(ll)]
        for i in range(ll):
            while st and T[st[-1]] < T[i]:
                index = st.pop()
                delay[index] = i - index
            st.append(i)

        # while st:  # 初始化为0的话 不用再次处理
        #     index = st.pop()
        #     delay[index] = 0

        return delay
a = Solution()
lst = [73,74,75,71,69,72,76,73]
print(a.dailyTemperatures(lst))