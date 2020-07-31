# ######################### 长度不超过m #######################################
"""
输入一个长度为n的整数序列，从中找出一段长度不超过m的连续子序列，
使得子序列中所有数的和最大。注意： 子序列的长度至少是1。
第一行输入两个整数n,m。
第二行输入n个数，代表长度为n的整数序列。
同一行数之间用空格隔开。
"""
from collections import deque
(n, m) = map(int, input().split())
num = list(map(int, input().split()))
# [1, -3, 5, 1, -2, 3]  m=4
# 问题转化：前缀和+优先队列
# 维护一个长度为m(区间长度)单调增序列，用右
prefix = [0] * (1+n)  # 前缀和
for i in range(1, n+1):
    prefix[i] += prefix[i-1] + num[i-1]
que = deque()
que.append(0)  # 单调队列
res = float("-inf")

for i in range(1, 1+n):
    # 宽度判断，直到i越界才会弹出表头，实际上相当于
    # i开始穿过整个窗口，后来一直在右边界
    if i - que[0] > m: que.popleft()
    res = max(res, prefix[i]-prefix[que[0]])  # 必须在这里处理，如果先压入，可能que[0]都没了
    while que and prefix[que[-1]] > prefix[i]:  # 假如前缀和比较大
        que.pop()
    que.append(i)
print(res)

"""
为什么要将prefix[0]初始化为0呢？
假如想计算1-3闭区间的和，用前缀和就是prefix[3]-prefix[0]
所以为了避免边界处理，需要初始化，而且要初始化为0
"""