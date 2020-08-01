"""
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。
每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量
不超过背包可承受的最大重量，且价值总和最大。输出最大价值。
输入格式
第一行两个整数，N，V,M，用空格隔开，分别表示物品件数、背包
容积和背包可承受的最大重量。接下来有 N 行，每行三个整数
vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。
"""
N, V, M = map(int, input().split())  # 数量 体积 重量
dp = [[0 for i in range(1+M)] for j in range(1+V)]
# 使用前i件物品，装二维限制(体积、重量)的背包能获得的最大价值
def zero_one_pack(dp, ci, mi, wi):
    for v in range(V, ci-1, -1):      # 体积约束
        for m in range(M, mi-1, -1):  # 承重约束
            # 用与不用比较，用的话获得新价值+体积损耗重量变小的包的价值
            dp[v][m] = max(dp[v][m], dp[v-ci][m-mi] + wi)

for i in range(N):
    (vi, mi, wi) = list(map(int, input().split()))
    zero_one_pack(dp, vi, mi, wi)
print(dp[-1][-1])
