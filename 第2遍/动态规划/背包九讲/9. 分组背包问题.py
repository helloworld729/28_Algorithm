"""
1、在一组物品内，定下一个体积，然后遍历所有的物品，取一个最大价值
这样每种体积都获得一个最优的商品

2、在不同组内，面对同一个体积，要么沿用要么替换用上一轮的小包+自己重新填充
无论哪种方式都保证在每一个体积位置，物品来自不同的包

3、v倒序是为了每个物品只取到最多一次，先体积，再物品数为了每组只选择一个
"""

(N, V) = list(map(int, input().split()))  # 数量 体积 重量
dp = [0 for i in range(1+V)]
for i in range(N):  # 每一组物品
    s = int(input())  # 商品数
    w_lst, v_lst = [], []
    for j in range(s):  # 必须对一组的物品暂存，贪心
        (vi, wi) = list(map(int, input().split()))
        w_lst.append(wi)
        v_lst.append(vi)
    for v in range(V, -1, -1):  # 遍历背包体积
        for k in range(len(w_lst)):  # 遍历物品
            # 此处与01背包的区别在于对一个体积位，考虑组内所有的物品
            if v-v_lst[k] > 0:
                dp[v] = max(dp[v], dp[v-v_lst[k]]+w_lst[k])
print(dp[-1])




