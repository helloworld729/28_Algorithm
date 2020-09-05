class Solution:  # 回溯做法
    def permutation(self, S: str):
        ll = len(S)
        if not ll: return [""]  # 不是空集

        res = []
        for i in range(ll):
            if S[i] in S[:i]:
                continue
            for sub in self.permutation(S[:i] + S[i+1:]):
                res.append(S[i] + sub)
        return res

a = Solution()
print(a.permutation("abb"))

# 思想:选择s[i]作为当前的第一个单词，其余的部分求排列

