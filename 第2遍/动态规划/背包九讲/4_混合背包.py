"""
有 N 种物品和一个容量是 V 的背包。
物品一共有三类：
第一类物品只能用1次（01背包）；
第二类物品可以用无限次（完全背包）；
第三类物品最多只能用 si 次（多重背包）；
每种体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
si=−1 表示第 i 种物品只能用1次；
si=0 表示第 i 种物品可以用无限次；
si>0 表示第 i 种物品可以使用 si 次；
"""
from collections import deque
N, V = map(int, input().split())
dp = [0] * (1+V)
que = deque()  # (位置，数据)

def zero_one_pack(dp, ci, wi):
    for v in range(V, ci-1, -1):
        dp[v] = max(dp[v], dp[v-ci]+wi)
def complete_pack(dp, ci, wi):
    for v in range(ci, V+1):
        dp[v] = max(dp[v], dp[v-ci]+wi)
def multi_pack(dp, ci, wi, si):
    k, s_back = 0, si
    while pow(2, k+1)-1 <= s_back:
        zero_one_pack(dp, pow(2, k)*ci, pow(2, k)*wi)
        si -= pow(2, k)
        k += 1
    if si > 0:
        zero_one_pack(dp, si * ci, si * wi)

for i in range(N):
    (v, w, s) = list(map(int, input().split()))
    if s == -1: zero_one_pack(dp, v, w)
    if s == 0: complete_pack(dp, v, w)
    if s > 0: multi_pack(dp, v, w, s)
print(dp[-1])