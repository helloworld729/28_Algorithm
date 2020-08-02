"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
类型：01背包，最大价值
特点：在线更新方式
"""
from copy import deepcopy
(N, V) = list(map(int, input().split()))
dp = [[0] * (V+1) for i in range(N)]
c_lst, w_lst = [], []
for i in range(N):
    (c, w) = list(map(int, input().split()))  # 体积(对应到列表要减1)，价值
    c_lst.append(c)
    w_lst.append(w)
count = -1
for (c, w) in zip(c_lst, w_lst):
    count += 1
    dp[count] = deepcopy(dp[count-1])
    for v in range(V, c-1, -1):  # 在线更新，v要>=c，才能使用c
        dp[count][v] = max(dp[count-1][v], dp[count-1][v-c]+w)  # 状态转移
for d in dp:
    print(d)
print(dp[-1])

res = []
# 编号序列
target = dp[-1][-1]
for i in range(N-1, 0, -1):  # 遍历物品
    for j in range(1, V+1, 1):  # 遍历体积
        if dp[i-1][j] + w_lst[i] == target:
            res.append(str(i+1))
            target -= w_lst[i]
            break
        elif dp[i-1][j] == target:
            if i-1 == 0:
                res.append(str(i))
            break
print(" ".join(res[::-1]))