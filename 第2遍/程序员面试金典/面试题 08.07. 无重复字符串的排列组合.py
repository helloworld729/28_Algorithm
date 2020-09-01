"""
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
"""
class Solution:
    def permutation(self, S: str):
        def permutate(s):
            ll = len(s)
            if ll == 1: return [s]
            temp = []
            for i in range(ll):
                first = s[i]
                for r in permutate(s[:i] + s[1+i:]):
                    if len(r) == s_len-1:
                        res.append(first + r)
                        # print(first + r, end=" ")
                    else: temp.append(first + r)
            return temp

        res = []
        s_len = len(S)
        permutate(S)

        return res


"""
方法1：选取第一个元素，剩余部分递归
"""
