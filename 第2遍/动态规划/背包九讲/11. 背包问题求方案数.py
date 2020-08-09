"""
有  N  件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出 最优选法的方案数。注意答案可能很大，请输出答案模 109+7 的结果。
"""
(N, V) = list(map(int, input().split()))
w_lst, v_lst = [], []

# dp[v] 体积为v的时候，最大的价值
dp = [0 for _ in range(V + 1)]

# dg[v] 填充体积v的时候，最大价值对应的最佳方案数目
dg = [0 for _ in range(V + 1)]
dg[0] = 1

for i in range(N):
    (vi, wi) = list(map(int, input().split()))
    w_lst.append(wi)
    v_lst.append(vi)

for i in range(N):
    for v in range(V, v_lst[i] - 1, -1):
        t = max(dp[v], dp[v - v_lst[i]] + w_lst[i])
        s = 0
        if t == dp[v]:
            s += dg[v]
        if t == dp[v - v_lst[i]] + w_lst[i]:
            s += dg[v - v_lst[i]]
        dp[v] = t
        dg[v] = s % (pow(10, 9)+7)
print(dp)
print(dg)

max_val = float("-inf")
res = 0
for d in dp:
    max_val = max(max_val, d)
for i in range(V + 1):
    if dp[i] == max_val:
        res += dg[i]
        res = res % (pow(10, 9)+7)
print(res)
