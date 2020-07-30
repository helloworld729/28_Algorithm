# ############################## 135. 最大子序和 ##############################
# https://www.acwing.com/problem/content/description/137/
from collections import deque
(n, m) = map(int, input().split())  # 总的物品数、总空间
num = []
for i in range(n):
    num.append(i)

res, que, r = [], deque(), 0        # 返回容器，单调队列，右边界初始化
for l in range(n - m + 1):  # 左边界推进
    if que and l > que[0]: que.popleft()
    while r < l + m:                      # 只在第一次会循环多次，后面只会一次
        cans = num[r]
        if que and cans > num[que[-1]]:  # 先把小数干掉
            while que and cans > num[que[-1]]:
                que.pop()
        # 全部干掉了，或者当前值不是最大的，但是窗口未满(下一轮就可能最大了，所以要保存)
        if len(que) < m: que.append(r)
        r += 1
    res.append(num[que[0]])
print(res)
