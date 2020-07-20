# 给出花园的数目和连接关系，给所有花园分配花的颜色，是的相连的花园
# 颜色不一样
# 邻接表、染色列表(assign)、颜色列表，遍历后继从颜色字典中祛除后继使用过的颜色即可
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        adjacent = collections.defaultdict(list)
        for vi, vj in paths:  # 临界字典
            adjacent[vi-1].append(vj-1)
            adjacent[vj-1].append(vi-1)
        garden_color = [0] * N
        for vi in range(N):
            colors = [1, 2, 3, 4]
            for vj in adjacent[vi]:
                if garden_color[vj] and garden_color[vj] in colors:
                    colors.remove(garden_color[vj])
            garden_color[vi] = colors[0]
        return garden_color
