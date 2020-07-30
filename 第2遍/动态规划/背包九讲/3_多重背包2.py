"""
有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
"""
# ############################## 单调队列 ################################
"""复杂度：V∑logS"""
(N, V) = map(int, input().split())  # 总的物品数、总空间
v_lst, w_lst, s_lst = [], [], []  # 体积、价值列表
for i in range(N):
    v, w, s = map(int, input().split())
    k, s_back = 0, s
    # 等比数列前k项的和为pow(2, k+1)-1，在逐步添加的过程中
    # 判断总量是否越界
    while pow(2, k+1)-1 <= s_back:
        v_lst.append(pow(2, k) * v)  # 耗费
        w_lst.append(pow(2, k) * w)  # 价值
        s -= pow(2, k)
        k += 1
    if s > 0:
        v_lst.append(s * v)  # 耗费
        w_lst.append(s * w)  # 价值

dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]
N = len(v_lst)
for i in range(N):  # 考虑第i件物品
    for v in range(V, v_lst[i]-1, -1):  # 当前考虑的容量
        dp[v] = max(dp[v], dp[v-v_lst[i]]+w_lst[i])
print(dp[-1])
