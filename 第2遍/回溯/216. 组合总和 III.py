# 求和限制：n
# 长度限制：k
# 数据：[1,2，... 9]
# 解集不能重复 + 解不含重复数字 --> cans[1+i:]

class Solution:
    def combinationSum3(self, k: int, n: int):
        candidates = list(range(1, 10))
        result = []

        def dfs(have, cans, have_lenth, have_sum):
            if have_sum == n and have_lenth == k:
                result.append(list(have))
                return
            if have_lenth >= k:  # 长度越界
                return

            ll = len(cans)
            for i in range(ll):
                if have_sum + cans[i] > n:  # 求和越界
                    break
                have.append(cans[i])
                dfs(have, cans[1+i:], have_lenth + 1, have_sum + cans[i])
                have.pop()

        dfs([], candidates, 0, 0)
        return result
