"""
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。
区间内的所有数字都在[0, 100]的范围内;
"""
ll = int(input())
nums = list(map(int, input().split()))
s = [0 for i in range(ll + 1)]  # 物理前缀和
for i in range(1, ll + 1):      # si表示前i个数据的和
    s[i] = s[i - 1] + nums[i-1]

min_num = [[0 for _ in range(ll)] for _ in range(ll)]
for i in range(ll):
    min_num[i][i] = nums[i]
for i in range(ll):
    for j in range(i + 1, ll):
        min_num[i][j] = min(min_num[i][j - 1], nums[j])

dp = [[0 for _ in range(ll)] for _ in range(ll)]  # 实际索引
ret = 0
for i in range(ll):
    dp[i][i] = nums[i] * nums[i]
    ret = max(ret, dp[i][i])

for i in range(ll-2, -1, -1):
    for j in range(i+1, ll):
        if nums[i] < min_num[i+1][j]:
            dp[i][j] = nums[i] * (nums[i] + s[j+1] - s[i+1])
        else:
            dp[i][j] = min_num[i][j] * nums[i] + dp[i + 1][j]
        ret = max(ret, dp[i][j])
print(ret)