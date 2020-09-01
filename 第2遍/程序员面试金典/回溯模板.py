"""
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
"""

class Solution:
    def permutation(self, S: str):
        result = []
        def back(cur, res):  # 当前的路径、可选的元素
            if len(res) == 0:
                result.append(''.join(cur))
                return
            for idx, charater in enumerate(res):  # 如果res不为空
                cur.append(charater)
                back(cur, res[:idx] + res[idx + 1:])  # 回溯
                cur.pop()

        back([], list(S))
        return result

    def permutation2(self, S: str):  # 传输做法
        result = []
        def back(cur, cans):  # 当前的路径、可选的元素
            if len(cans) == 0:
                result.append(cur)
                return
            for idx, charater in enumerate(cans):  # 如果res不为空
                cur += charater
                back(cur, cans[:idx] + cans[idx + 1:])  # 回溯
                cur = cur[:-1]

        back("", S)
        return result



a = Solution()
print(a.permutation2("abcde"))