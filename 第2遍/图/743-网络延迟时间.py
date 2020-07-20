from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        adjacent = defaultdict(list)
        path = {}
        for vi, vj, time in times:
            adjacent[vi].append((time, vj))
        cans = [(0, K)]
        count = 0

        while count < N and cans:
            ti, vi = cans.pop()
            if vi in path:  # 一定加这个，否则count的存在会导致没有求所有节点的最短路径
                continue
            path[vi] = ti
            count += 1
            for time, vj in adjacent[vi]:
                if vj not in path:  # 这里也要注意
                    cans.append((time + ti, vj))
            cans.sort(reverse=True)

        return max(path.values()) if len(path) == N else -1

# times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
# a = Solution()
# print(a.networkDelayTime(times, 5, 5))

# 堆优化：
# ti, vi = heapq.heappop(cans)  # 出堆  VS cans.pop()
# heapq.heappush(cans, (time + ti, vj))  # 入堆  VS cans.append((time + ti, vj))  and cans.sort()


