"""
有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
为了便于处理，在dp前垫了一个0，这样dp[i]就是指空间为i的背包
"""
# ############################## 单调队列 ################################
from collections import deque
N, V = map(int, input().split())
dp = [0] * (1+V)
que = deque()  # (位置，数据)
for i in range(N):
    (v, w, s) = list(map(int, input().split()))
    for j in range(v):  # 余数划分,每个物品都会更新完所有的位置
        que.clear()
        for k in range(0, (V-j) // v + 1):  # 序列长度
            if que and k - que[0][0] > s: que.popleft()  # 最大值是否越界
            rest = dp[j + k * v] - k * w
            while que and que[-1][1] < rest:
                que.pop()
            que.append((k, rest))
            dp[j + k * v] = que[0][1] + k * w
print(dp[V])

