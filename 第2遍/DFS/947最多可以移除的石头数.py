# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/15 11:52
# 输入是坐标二维列表，元素表示石头的位置，同行或者同列的石头可以
# 移除其中一个，然后继续，问最多可以移除多少个石头。
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()

        def dfs(node):
            if tuple(node) in visited: return
            visited.add(tuple(node))
            x, y = node
            for stone in stones:
                if x == stone[0] or y == stone[1]:
                    dfs(stone)

        count = 0
        for s in stones:
            if tuple(s) not in visited:
                count += 1
                dfs(s)

        return len(stones) - count

stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]

print(Solution().removeStones(stones))

# 思路：在同一行或者同一列的石头相互连通，用dfs的方法标记整个连通集
# 因为每个联通集最后剩下一个石头，所以问题转化为求联通集合的数目

# node：不能直接判断list是否在哈希set中，需要先转化为tuple，不能直接
# 使用str(list[0])+str(list[1])这种写法，因为 [3，33]和[33，3]会被认为
# same，所以要么加下划线，要么直接使用tuple(list)




