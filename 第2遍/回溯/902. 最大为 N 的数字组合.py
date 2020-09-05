"""
题目：
我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 
的非空子集。（请注意，'0' 不包括在内。）
现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 
D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。
返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。
链接：https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set
"""

class Solution:
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)  # 总长
        dp = [0] * K + [1]  # 防止第63行边界处理
        # dp[i]：从末位到当前位的合法数目

        for i in range(K-1, -1, -1):
            # Compute dp[i]
            for d in D:  # 表示以d填充第i位的话
                if d < S[i]:  # 如果d比较小，后续各位任意
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:  # 相等的话
                    dp[i] += dp[i+1]
                else: break

        return dp[0] + sum(len(D) ** i for i in range(1, K))


"""
当[1，2，3，4],238的时候

'1', '2','3','4',

'11', '12', '13', '14',
'21', '22', '23', '24',
'31', '32', '33', '34', 
'41', '42', '43', '44'
 
'111', '112', '113', '114',
'121', '122', '123', '124',  
'131', '132', '133', '134',  
'141', '142', '143', '144',   

'211', '212', '213', '214', 
'221', '222', '223', '224',  
'231', '232', '233', '234',   
"""
# 首先，下面这种解法延续了了模板的思路
# 但是结果超时，因为这个题已经不再是之前的类型，可以通过长度直接判定
# 而不需要求和
def atMostNGivenDigitSet(digits, n: int):
    result = []
    n_len = len(str(n))
    global count
    count = 0

    def compair(a):  # 如果a小返回True
        ll = len(a)
        if not ll: return True
        if ll < n_len:
            return True
        elif ll > n_len:
            return False
        else:
            return int(a) <= n

    def dfs(have, cans):
        if compair(have):
            global count
            count += 1
            result.append(have)
        ll = len(cans)
        for i in range(ll):
            if not compair(have + cans[i]):  # 求和越界
                break
            have += cans[i]
            dfs(have, cans)
            have = have[:-1]

    dfs("", digits)
    print(count - 1)
    return result

# D = ["1","2","3","4"]
# N = 238
# print(atMostNGivenDigitSet(D, N))
# 全局变量需要在外部声明吗，还是在内部使用的时候再声明就行
