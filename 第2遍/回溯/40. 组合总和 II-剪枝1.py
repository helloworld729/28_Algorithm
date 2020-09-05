"""只能使用一次 + 解集不能重复"""

def combinationSum2(candidates, target: int):
    result = []  # 排列组合出所有的可能
    candidates.sort()  # 排序
    def advanced(have, cans, have_sum):
        ll = len(cans)
        if have_sum == target:
            result.append(list(have))
            return
        if have_sum > target:  # 一定要剪枝
            return

        visited = {}
        for i in range(ll):
            if cans[i] in visited:
                continue
            if have_sum + cans[i] > target:
                break
            visited[cans[i]] = 1
            have.append(cans[i])

            advanced(have, cans[1+i:], have_sum + cans[i])
            have.pop()

    advanced([], candidates, 0)
    return result


candidates = [2,5,2,1,2]
print(combinationSum2(candidates, 5))

# 无重复推进模板 + 剪枝 + 哈希

