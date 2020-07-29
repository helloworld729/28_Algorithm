
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# ########################## 最长回文子串 leetcode-5 ######################################
# 从右到左计算
def longestPalindrome(s: str) -> str:
    if not s:
        return
    leng = len(s)
    dp = [[0] * leng for _ in range(leng)]
    dp[0][0] = True
    tar = []  # 目标子串区间
    diff = 0  # 子串长度
    for i in range(1, leng):  # 以右边界为i，左边界为j
        for j in range(i + 1):
            if i == j:
                dp[i][j] = True
            elif j == (i - 1):
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i - 1][j + 1] and (s[i] == s[j])

            if dp[i][j] and i-j > diff:
                tar = [j, i]
                diff = i - j
    for data in dp:
        print(data)

    print(tar)
    if tar:
        print(s[tar[0]: tar[1]+1])
    else:
        print(s[0])

# longestPalindrome('abahijkkjihdd')

# ########################## 机器人路径搜索 leetcode-62 ######################################
def uniquePaths(m: int, n: int) -> int:
    if m*n == max(m,n):
        return 1
    dp = [[0] * (n-1) + [1] for _ in range(m-1)]
    dp.append([1] * n)
    # for i in dp:
    #     print(i)
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
    for i in dp:
        print(i)

# uniquePaths(3,2)
# ########################## 分治法路径搜索 leetcode-62 ######################################

def uniquePaths2(m: int, n: int) -> int:
    """超时了"""
    def search(i, j):
        if i >= m or j >=n:
            return 0
        elif i == m-1 and j == n-1:
            return 1
        return search(i, j+1) + search(i+1, j)
    return search(0,0)

# print(uniquePaths2(6,5))



# 20200728





