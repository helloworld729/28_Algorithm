"""
有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
第 i 种物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
"""
(N, V) = map(int, input().split())  # 总的物品数、总空间
v_lst, w_lst = [], []  # 体积、价值列表
for i in range(N):
    v, w = map(int, input().split())
    v_lst.append(v)
    w_lst.append(w)

dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]

for i in range(N):  # 考虑第i件物品
    for v in range(v_lst[i], V+1):  # 当前考虑的容量
        dp[v] = max(dp[v], dp[v-v_lst[i]]+w_lst[i])
        # print(v, dp)
print(dp[-1])
