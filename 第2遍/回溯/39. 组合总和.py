"""无重复数组 + 元素无限使用 + 解集不能重复"""
class Solution:
    def combinationSum(self, candidates, target: int):
        """迭代解法"""
        res = []
        st = []
        ll = len(candidates)
        for i in range(ll):
            if candidates[i] <= target:
                st.append([[candidates[i]], target - candidates[i], i])  # 已经有的值，还需要的值,索引

        while st:
            combine, need, index = st.pop()
            if need == 0:
                res.append(combine)
            if need > 0:
                for j in range(index, ll):
                    num = candidates[j]
                    if num <= need:
                        st.append([combine+[num], need - num, j])
        return res

    def combinationSum2(self, candidates, target):
        """递归模板解法"""
        result = []  # 排列组合出所有的可能
        candidates.sort()  # 排序

        def advanced(have, cans, have_sum):
            ll = len(cans)
            if have_sum == target:
                result.append(list(have))
                return

            # visited = {}
            for i in range(ll):
                # if cans[i] in visited:
                #     continue
                if have_sum + cans[i] > target:  # 剪枝
                    break
                # visited[cans[i]] = 1
                have.append(cans[i])
                advanced(have, cans[i:], have_sum + cans[i])  # 从当前index考虑
                have.pop()

        advanced([], candidates, 0)
        return result


"""
输入：candidates = [2,3,6,7], target = 7,
所求解集为：[ [7], [2,2,3]]

无重复：不用哈希
无限使用 + 结果去重：考虑从当前index到末尾
"""