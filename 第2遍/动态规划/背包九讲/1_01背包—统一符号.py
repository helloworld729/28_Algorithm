"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
类型：01背包，最大价值
特点：在线更新方式
"""
(N, V) = list(map(int, input().split()))
dp = [0] * (V+0)

for i in range(N):
    (c, w) = list(map(int, input().split()))  # 体积(对应到列表要减1)，价值
    for v in range(V-1, c-1, -1):  # 在线更新，v要>=c，才能使用c
        dp[v] = max(dp[v], dp[v-c]+w)  # 状态转移
    print(dp)
print(dp[-1])

# 为什么dp要加0？
# dp前面加0的话，dp[i]可以表示背包容量为i
