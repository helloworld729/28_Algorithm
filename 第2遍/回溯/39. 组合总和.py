"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[  [7],  [2,2,3]]
链接：https://leetcode-cn.com/problems/combination-sum

方法：为了避免重复，只能考虑后面的数字，
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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