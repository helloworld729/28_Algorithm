"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
类型：01背包，最大价值
特点：在线更新方式
"""

(N, V) = list(map(int, input().split()))
dp = [[0] * (V+1) for i in range(N+1)]
v_lst, w_lst = [0], [0]
for i in range(N):
    (c, w) = list(map(int, input().split()))  # 体积(对应到列表要减1)，价值
    v_lst.append(c)
    w_lst.append(w)
for i in range(N, 0, -1):
    for j in range(V, v_lst[i]-1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j-v_lst[i]]+w_lst[i])
print(dp)





