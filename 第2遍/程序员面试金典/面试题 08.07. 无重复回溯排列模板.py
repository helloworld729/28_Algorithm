"""
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
"""
class Solution:  # 回溯做法
    def permutation(self, S: str):
        ll = len(S)
        if not ll: return [""]  # 不是空集

        res = []
        for i in range(ll):
            for sub in self.permutation(S[:i] + S[i+1:]):
                res.append(S[i] + sub)
        return res

a = Solution()
print(a.permutation("abc"))