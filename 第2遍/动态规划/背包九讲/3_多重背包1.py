"""
有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
"""
# ############################## 转化为01背包##################################
"""复杂度：V∑S"""
# (N, V) = map(int, input().split())  # 总的物品数、总空间
# dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]
#
# def zero_one_pack(dp, ci, wi):
#     for v in range(V, ci - 1, -1):
#         dp[v] = max(dp[v], dp[v - ci] + wi)
#
# for i in range(N):
#     v, w, s = map(int, input().split())
#     for j in range(s):
#         zero_one_pack(dp, v, w)
#
# print(dp[-1])
# ############################## 二进制优化时空 ################################
"""复杂度：V∑logS"""
(N, V) = map(int, input().split())  # 总的物品数、总空间
dp = [0] * (1 + V)  # 为了递推公式兼容dp[1]，有必要设置dp[0]

def zero_one_pack(dp, ci, wi):
    for v in range(V, ci - 1, -1):
        dp[v] = max(dp[v], dp[v - ci] + wi)

for i in range(N):
    v, w, s = map(int, input().split())
    k, s_back = 0, s
    while pow(2, k + 1) - 1 < s_back:
        zero_one_pack(dp, pow(2, k) * v, pow(2, k) * w)
        s -= pow(2, k)
        k += 1
    if s > 0:
        zero_one_pack(dp, s * v, s * w)

print(dp[-1])

"""
关于二进制拆分：
pow(2,0)+pow(2,1)+pow(2,2)+pow(2,3)+......pow(2,k)
将k初始化为0，并逐渐的增加到当前的k，总和为pow(2, k+1)-1，
以此来判断当前的值加进去会不会越界。
例如第一次使用1去判断，第二次不是用2，而是3
一定要注意：由于先对s减去2的k次，所以k的更新要放到后面
"""