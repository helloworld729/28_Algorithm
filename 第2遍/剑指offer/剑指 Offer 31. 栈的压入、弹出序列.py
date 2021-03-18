from typing import List
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,
# 5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 用一个栈
        # 如果栈顶 != 出栈指针  压栈
        # 如果栈顶 == 出栈指针  出栈
        length1 = len(pushed)
        length2 = len(popped)
        if length2 != length1: return False

        back = []
        p1 = p2 = 0

        while p1 <= length1 - 1 and p2 <= length2 - 1:
            if (p1 == 0 and p2 == 0):
                back.append(pushed[p1])
                p1 += 1
            elif (not back) or (popped[p2] != back[-1]):  # 入栈
                back.append(pushed[p1])
                p1 += 1
            else:
                popped[p2] == back[-1]  # 出栈
                p2 += 1
                back.pop()

        while p2 <= length2 - 1:
            if not (popped[p2] == back[-1]):
                return False
            back.pop()
            p2 += 1

        return not back
