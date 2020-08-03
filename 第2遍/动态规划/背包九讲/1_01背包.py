# ############################ 一维解法 #################################################
(N, V) = map(int, input().split())  # 总的物品数、总空间
v_lst, w_lst = [], []  # 体积、价值列表
for i in range(N):
    v, w = map(int, input().split())
    v_lst.append(v)
    w_lst.append(w)

dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]

for i in range(N):  # 考虑第i件物品
    for distribute in range(V, v_lst[i]-1, -1):  # 当前考虑的容量(中间减一因为右开区间)
        dp[distribute] = max(dp[distribute], dp[distribute - v_lst[i]] + w_lst[i])
print(dp[-1])

# ############################二维解法 #################################################
(N, V) = list(map(int, input().split()))
dp = [[0 for _ in range(1+V)] for _ in range(N)]
v_lst, w_lst = [], []

for j in range(N):
    (vi, wi) = list(map(int, input().split()))
    v_lst.append(vi)
    w_lst.append(wi)

for i in range(N):
    for v in range(V, -1, -1):
        dp[i][v] = dp[i-1][v]  # very important
        if v >= v_lst[i]:
            dp[i][v] = max(dp[i-1][v], dp[i-1][v-v_lst[i]]+w_lst[i])
print(dp[-1][-1])

# ############################ 二维online解法 ###########################################
(N, V) = list(map(int, input().split()))
dp = [[0 for _ in range(1+V)] for _ in range(N)]

for i in range(N):
    (vi, wi) = list(map(int, input().split()))
    for v in range(V, -1, -1):
        dp[i][v] = dp[i-1][v]
        if v >= vi:
            dp[i][v] = max(dp[i-1][v], dp[i-1][v-vi]+wi)

print(dp[-1][-1])

