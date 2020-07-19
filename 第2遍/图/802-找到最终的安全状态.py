"""
802. 找到最终的安全状态
安全节点的情况：
1、出度为0 ；2、后继全都是出度为0的点；3、后继全部属于2
那么反过来就是
1、入度为0；2、前驱全都是入度为0；3、前驱全部属于2
这就转化为拓扑排序，其实不转化也可以，只不过拓扑排序常见
"""
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph):

        zero_degree = deque()
        in_degree = {i: 0 for i in range(len(graph))}
        adjacent = {i: [] for i in range(len(graph))}

        for vi, vjs in enumerate(graph):
            for vj in vjs:
                adjacent[vj].append(vi)
                in_degree[vi] += 1

        for i in range(len(graph)):
            if in_degree[i] == 0:
                zero_degree.append(i)

        res = []
        while zero_degree:
            vi = zero_degree.popleft()
            res.append(vi)
            for vj in adjacent[vi]:
                in_degree[vj] -= 1
                if in_degree[vj] == 0:
                    zero_degree.append(vj)
        res.sort()
        return res

# 方法2 去除排序
from collections import deque
class Solution2:
    def eventualSafeNodes(self, graph):
        zero_degree = deque()
        res = [False for i in range(len(graph))]
        in_degree = {i: 0 for i in range(len(graph))}
        adjacent = {i: [] for i in range(len(graph))}

        for vi, vjs in enumerate(graph):
            for vj in vjs:
                adjacent[vj].append(vi)
                in_degree[vi] += 1

        for i in range(len(graph)):
            if in_degree[i] == 0:
                zero_degree.append(i)

        while zero_degree:
            vi = zero_degree.popleft()
            res[vi] = True
            for vj in adjacent[vi]:
                in_degree[vj] -= 1
                if in_degree[vj] == 0:
                    zero_degree.append(vj)
        return [i for i, j in enumerate(res) if j]