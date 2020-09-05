""" 输入：S = "qwe" 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]"""

class Solution:
    def permutation(self, S: str):
        result = []     # 结果列表
        def back(cur, res):  # 当前的路径、可选的元素
            if len(res) == 0:
                result.append(''.join(cur))
                return
            for idx, charater in enumerate(res):  # 如果res不为空
                cur.append(charater)
                back(cur, res[:idx] + res[idx + 1:])
                cur.pop()

        back([], list(S))
        return result

a = Solution()
print(a.permutation("abc"))