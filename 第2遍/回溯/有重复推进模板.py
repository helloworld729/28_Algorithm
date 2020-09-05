""" 输入：S = "abb" 输出：["abb", "bab", "bba"]"""

class Solution:
    def permutation(self, S: str):
        result = []     # 结果列表
        def advance(cur, cans):  # 当前的路径、可选的元素
            if len(cans) == 0:
                result.append(''.join(cur))
                return
            for idx, charater in enumerate(cans):  # 如果cans不为空
                if cans[idx] in cans[:idx]:
                    continue
                cur.append(charater)
                advance(cur, cans[:idx] + cans[idx + 1:])
                cur.pop()

        advance([], list(S))
        return result

a = Solution()
print(a.permutation("abb"))


# 第13行不写成 if S[idx] in S[:idx]，必须面向当前可选的序列
# 因为在推进的过程中，候选序列时刻在变短，对根据S来判断是没有
# 道理的。
# 推进比回溯要快很多，优先选择推进。
