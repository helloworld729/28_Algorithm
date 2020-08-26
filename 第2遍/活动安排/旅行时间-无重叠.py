def max_overlap(lst):
    back = []
    for i in range(len(lst)):
        back.append((lst[i][0], 0))  # 用0标识是 开始时间
        back.append((lst[i][1], 1))  # 用1标识是 结束时间
    back.sort()
    count = 0
    res = 0
    for j in range(len(back)):
        if back[j][1] == 0:
            count += 1
            res = max(res, count)
        else:
            count -= 1
    return res

lst = [
    [1,9], [2,8], [8,9]
]
print(max_overlap(lst))

"""
题目：给出一系列的时间边界，求解那一天能够去旅行的话去的话人最多，输出这个count
思路：对所有时间统一排序，然后在遍历的过程中遇到开始时间就对count+1，否则对count-1

细节：假如序列没有重叠的话，算法是没有问题的
      假如出现某一天是a的结束时间，是b的开始时间，这种情况下如果要求加2，则需保证排序的
      结果开始标识的要排在前面，例如本题已经采取的方案。别的情况的变化可以通过改变标识
      的办法来实现。
      
结果：时间复杂度为O(NlogN)，空间复杂度为O(N)
"""