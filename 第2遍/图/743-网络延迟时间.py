from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        adjacent = defaultdict(list)
        path = []
        for vi, vj, time in times:
            adjacent[vi].append((vj, time))
        cans = [(0, K)]
        count = 0
        while count < N and cans:
            count += 1
            ti, vi = cans.pop()
            path.append(ti)
            for vj, time in adjacent[vi]:
                cans.append((time + ti, vj))
            cans.sort(reverse=True)
        print(path)
        if len(path) < N:
            return -1
        else:
            return max(path)

time = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
a = Solution()
print(a.networkDelayTime(time, 3, 1))