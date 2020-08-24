# ############################## 135. 最大子序和 ##############################
"""
输入一个长度为n的整数序列，从中找出一段长度不超过m的 连续子序列，
使得子序列中所有数的和最大。注意： 子序列的长度至少是1。
输入格式
第一行输入两个整数n,m。
第二行输入n个数，代表长度为n的整数序列。
同一行数之间用空格隔开。
输出格式
输出一个整数，代表该序列的最大子序和。
"""
# https://www.acwing.com/problem/content/description/137/
from collections import deque
(n, m) = map(int, input().split()) 
num = list(map(int, input().split()))

res, que, r = 0, deque(), 0        # 返回容器，单调队列，右边界初始化
for l in range(n - m + 1):  # 左边界推进
    if que and l > que[0]: que.popleft()
    while r < l + m:                      # 只在第一次会循环多次，后面只会一次
        cans = num[r]
        if cans > 0:   # 遇到正值
            que.append(r)
            while que[0] < 0:
                que.popleft()
        else:          # 遇到负值
            if not que:
                que.append(r)  # 空栈压入
            elif que[-1] < cans:  # 最多保留一个负值
                que.pop()
                que.append(r)
        r += 1
    print(que)


