class Solution:  # 回溯做法
    def permutation(self, S: str):
        ll = len(S)
        if not ll: return [""]  # 不是空集
        # if ll == 1: return [S]

        res = []
        for i in range(ll):
            if S[i] in S[:i]:
                continue
            for sub in self.permutation(S[:i] + S[i+1:]):
                res.append(S[i] + sub)
        return res

a = Solution()
print(a.permutation("abc"))
