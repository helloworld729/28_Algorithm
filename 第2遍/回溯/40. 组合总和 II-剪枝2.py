def combinationSum2(candidates, target: int):
    result = []  # 排列组合出所有的可能
    candidates.sort()  # 排序
    def advanced(have, cans, have_sum):
        ll = len(cans)
        if have_sum == target:
            result.append(list(have))
            return

        visited = {}
        for i in range(ll):
            if cans[i] in visited:
                continue
            if have_sum + cans[i] > target:  # 为什么必须放到这里
                break
            visited[cans[i]] = 1
            have.append(cans[i])
            advanced(have, cans[1+i:], have_sum + cans[i])
            have.pop()

    advanced([], candidates, 0)
    return result

candidates = [2,5,2,1,2]
print(combinationSum2(candidates, 5))

# 和上一段代码的区别在于剪枝的时机不同。
# 关于break的时机，一定要在have的append操作之前，因为在不同的递归层中
# have是公用的，下层返回到上层之前要把have恢复，为了避免只压栈，不弹出
# 必须在压栈之前判断

