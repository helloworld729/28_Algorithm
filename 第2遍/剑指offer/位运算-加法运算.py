# 计算1+2+3+...+n
# 逻辑运算递归计算

class Solution:
    def __init__(self):
        # 设置全局变量, 方法1需要
        self.res = 0


    def sumNums(self, n: int) -> int:
        # 逻辑开关
        n > 0 and self.sumNums(n-1)
        self.res += n
        return self.res

    def methodTwo(self, n:int) -> int:
        # 俄罗斯农民算法
        count = 0  # 右移次数
        res = 0    # 返回结果
        num = n    # 输入参数
        while n:
            if n & 1:
                res += (1+num) << count
            n >>= 1
            count += 1
        return res >> 1

for i in range(5):
    print(Solution().sumNums(i))
    print(Solution().methodTwo(i))

