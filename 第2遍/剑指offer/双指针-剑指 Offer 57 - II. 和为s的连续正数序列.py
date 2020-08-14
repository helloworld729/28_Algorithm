"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
输入：target = 9
输出：[[2,3,4],[4,5]]
方法1:折半遍历，超时
方法2：双指针，非常秒 由于两个边界单调不减时间负复杂度为O(target)
"""
from collections import deque
class Solution:
    def findContinuousSequence(self, target: int):
        ll = target//2 + 1 + 1
        s = [0 for i in range(ll)]
        for i in range(1, ll):
            s[i] += s[i-1] + i

        res = []
        for i in range(target // 2 + 1, 0, -1):
            if s[i] < target: break
            for j in range(i-2, -1, -1):
                if s[i] - s[j] == target:
                    res.append(list(range(j+1, i+1)))
                    break
        return res[::-1]

    def findContinuousSequence2(self, target: int):
        que = deque()
        l, r = 1,2
        total = l + r
        res = []
        que.append(l)
        que.append(r)

        while l != r:
            if total == target:
                res.append(list(que))
                que.popleft()  # 保存之后，一定要将左边界推进
                total -= l
                l += 1
            if total < target:
                r += 1
                total += r
                que.append(r)
            elif total > target:
                que.popleft()
                total -= l
                l += 1
        return res


a = Solution()
print(a.findContinuousSequence(502))