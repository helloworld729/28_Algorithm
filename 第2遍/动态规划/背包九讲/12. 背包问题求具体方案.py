"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出 字典序最小的方案。这里的字典序是指：所选物品的编号所构成的序列。物品的编号范围是 1…N。
以前: dp[i,j] 前i件物品中装一个体积为j的包，能获得的最大价值
现在：dp[i,j] 从i到最后的所有物品中装一个体积为j的包，能获得的最大价值
"""
(n, m) = list(map(int, input().split()))
w_lst, v_lst = [], []
dp = [[0 for _ in range(m+1)]for _ in range(n+1)]

for i in range(n):
    (vi, wi) = list(map(int, input().split()))
    w_lst.append(wi)
    v_lst.append(vi)

# 根据递推公式知道物品要倒排
# 因为是二维数组，所以体积的顺序正反都可以
for i in range(n-1, -1, -1):  # good
    for j in range(1, m+1):   # volumn
        dp[i][j] = dp[i+1][j]  # 重要
        if j >= v_lst[i]:  # 注意等号
            dp[i][j] = max(dp[i][j], dp[i+1][j-v_lst[i]]+w_lst[i])

cur_v = m
res = []
for i in range(n):
    if dp[i][cur_v] == dp[i+1][cur_v-v_lst[i]]+w_lst[i]:
        res.append(str(i+1))
        cur_v -= v_lst[i]
print(" ".join(res))

