from typing import List
import collections
class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        # 问题转化为统计连通分量的个数
        if len(edges) < n - 1: return -1
        visited = set()

        adjacent = collections.defaultdict(list)
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        def dfs(node):
            visited.add(node)
            for n2 in adjacent[node]:
                if n2 not in visited:
                    dfs(n2)

        unions = n - len(adjacent)

        for k, v in adjacent.items():
            if k not in visited:
                unions += 1
            dfs(k)

        return unions - 1



edges = [[0,1],[0,2],[0,3],[1,2],[1,3]]

print(Solution().makeConnected(6, edges))