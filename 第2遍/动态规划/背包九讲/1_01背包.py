(N, V) = map(int, input().split())  # 总的物品数、总空间
v_lst, w_lst = [], []  # 体积、价值列表
for i in range(N):
    v, w = map(int, input().split())
    v_lst.append(v)
    w_lst.append(w)

res = 0  #
dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]

for i in range(N):  # 考虑第i件物品
    for distribute in range(V, v_lst[i]-1, -1):  # 当前考虑的容量(中间减一因为右开区间)
        dp[distribute] = max(dp[distribute], dp[distribute - v_lst[i]] + w_lst[i])
        res = max(res, dp[distribute])
    print(dp)
print(res)

