from collections import deque
from collections import defaultdict
from copy import copy,deepcopy
# ############################### 207 课程表 ############################################
"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。例如，想要学习课程0,你需要先完成课程1，
我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习

示例 1:
输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

思路：拓扑排序[零度队列或者零度链表]
链接：https://leetcode-cn.com/problems/course-schedule
"""
def canFinish_que(self, numCourses: int, prerequisites) -> bool:
    indegrees = [0 for _ in range(numCourses)]   # 入度表
    adjacency = [[] for _ in range(numCourses)]  # 邻接表
    queue = deque()
    # Get the indegree and adjacency of every course.
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    # Get all the courses with the indegree of 0.
    for i in range(len(indegrees)):  #　零度队列
        if not indegrees[i]: queue.append(i)
    # BFS TopSort.
    while queue:
        pre = queue.popleft()
        numCourses -= 1
        for cur in adjacency[pre]:  # cur may empty
            indegrees[cur] -= 1
            if not indegrees[cur]: queue.append(cur)
    return not numCourses

def canFinish_link(self, numCourses: int, prerequisites) -> bool:
    in_degree = [0 for i in range(numCourses)]  # 入度表
    adjacent = [[] for i in range(numCourses)]  # 邻接表(后继)
    zero_v = -1  # zero link
    for latter, formmer in prerequisites:
        in_degree[latter] += 1
        adjacent[formmer].append(latter)
    for vi in range(numCourses):
        if in_degree[vi] == 0:
            in_degree[vi] = zero_v
            zero_v = vi
    while zero_v != -1:
        vi = zero_v
        zero_v = in_degree[vi]
        numCourses -= 1
        for vj in adjacent[vi]:
            in_degree[vj] -= 1
            if in_degree[vj] == 0:  # 入度为0
                in_degree[vj] = zero_v
                zero_v = vj
    return not numCourses

# ############################### 310 最小高度树 ############################################
# 类似于拓扑排序
def findMinHeightTrees(n: int, edges):
    adjacent = [[] for i in range(n)]  # 邻接表
    tree_height = {i: 0 for i in range(n)}  # 树高字典
    for i, j in edges:
        adjacent[i].append(j)
        adjacent[j].append(i)
    def dijskra(vo):
        path = [None for _ in range(n)]
        count = 0
        cans = [(0, vo, vo)]
        while count < n and cans:
            distance, vi, vj = cans.pop()
            if path[vj]: continue
            path[vj] = distance
            for vk in adjacent[vj]:
                if path[vk] is None:
                    cans.append((distance + 1, vj, vk))
            cans.sort(reverse=True)
        return path
    for i in range(n):
        path = dijskra(i)
        path.sort()
        tree_height[i] = path[-1]
    ret = sorted(tree_height.items(), key=lambda x: x[1])
    dis_mem = ret[0][1]
    res = []
    for v, dis in ret:
        if dis == dis_mem:
            res.append(v)
        else:
            break
    return res
# 超时
###################### 1092
def findMinHeightTrees2(n: int, edges):
    if n <= 2:
        return list(range(n))
    degree = [0 for _ in range(n)]  # 度表
    adjacent = [[] for _ in range(n)]  # 邻接表
    for i, j in edges:
        adjacent[i].append(j)
        degree[i] += 1
        degree[j] += 1
        adjacent[j].append(i)
    cans = list(range(n))
    one_d = []
    for i in range(n):  # 度为1
        if degree[i] == 1:
            one_d.append(i)
            cans.remove(i)
    if len(cans) <= 2:
        return cans
    while True:
        new_one = []
        while one_d:
            vi = one_d.pop()  # 节点索引
            for vj in adjacent[vi]:
                degree[vj] -= 1
                if degree[vj] == 1 and vj in cans:
                    cans.remove(vj)
                    new_one.append(vj)
        one_d =new_one
        if len(cans) <= 2:
            return cans
###################### 372
def findMinHeightTrees3(n: int, edges):
    if n <= 2:
        return list(range(n))
    degree = [0 for _ in range(n)]  # 度表
    adjacent = [[] for _ in range(n)]  # 邻接表
    for i, j in edges:
        adjacent[i].append(j)
        degree[i] += 1
        degree[j] += 1
        adjacent[j].append(i)
    cans = {i:degree[i] for i in range(n)}
    one_d = []
    for i in range(n):  # 度为1
        if degree[i] == 1:
            one_d.append(i)
            del cans[i]
    if len(cans) <= 2:
        return list(cans.keys())
    while True:
        new_one = []
        while one_d:
            vi = one_d.pop()  # 节点索引
            for vj in adjacent[vi]:
                degree[vj] -= 1
                if degree[vj] == 1 and vj in cans:
                    del cans[vj]
                    new_one.append(vj)
        one_d = new_one
        if len(cans) <= 2:
            return list(cans.keys())
########################## 304 0.63
def findMinHeightTrees4(n: int, edges):
    if n <= 2: return list(range(n))
    adjacent = defaultdict(list)  # 邻接表
    for i, j in edges:
        adjacent[i].append(j)
        adjacent[j].append(i)
    one_degree = [i for i in adjacent if len(adjacent[i]) == 1]
    while n > 2:
        new_one = []
        for vi in one_degree:
            vj = adjacent[vi].pop()
            adjacent[vj].remove(vi)
            if len(adjacent[vj]) == 1:
                new_one.append(vj)
            n -= 1
        one_degree = new_one
    return new_one

# lst = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# print(findMinHeightTrees2(6, lst))

#
def findItinerary0(tickets):
    adjacent = defaultdict(list)
    for f, t in tickets:
        adjacent[f].append(t)
    for key in adjacent.keys():
        adjacent[key].sort()
    res = ["JFK"]
    all_plans = []

    def dfs(plan, adjacent):
        if len(plan) == len(tickets) + 1:
            all_plans.append(plan)
            return
        cans = adjacent[plan[-1]]
        for next_pos in cans:
            if len(all_plans) == 0:  # 放在倒2或者for之前都没有这里快
                plan_now = list(plan)  # 不能影响后续的plan
                adjacent_now = deepcopy(adjacent)
                adjacent_now[plan[-1]].remove(next_pos)
                plan_now.append(next_pos)
                dfs(plan_now, adjacent_now)

    dfs(res, adjacent)
    return all_plans[0]


# 递归边界条件与提前终止
# 边界：目标条件(长度要求)
# 提前终止：外部变量

def findItinerary(tickets):
    adjacent = defaultdict(list)
    for f, t in tickets:
        adjacent[f].append(t)
    for key in adjacent.keys():
        adjacent[key].sort(reverse=True)
    all_plans = []
    def dfs(pos_now):
        while adjacent[pos_now]:
            pos_next = adjacent[pos_now].pop()
            dfs(pos_next)
        all_plans.append(pos_now)
    dfs("JFK")
    return all_plans[::-1]
# tickets =  [["JFK", "C"], ["JFK", "B"], ["C", "JFK"], ]
# tickets =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# res = findItinerary(tickets)
# print(res)
def eventualSafeNodes0(graph):
    adjacent = defaultdict(list)
    terminal = []
    for v, next in enumerate(graph):
        for pos in next:
            adjacent[v].append(pos)
    for v, next in enumerate(graph):
        if len(next) == 0:
            terminal.append(v)

    def dfs(path, v):
        if v in terminal:
            global end_flag
            end_flag = True
            return
        for next_pos in adjacent[v]:
            global circle_flag
            if next_pos in path:
                # global circle_flag
                circle_flag = True
                path.append(next_pos)
                break
            if not circle_flag:
                new_path = list(path)
                new_path.append(next_pos)
                dfs(new_path, next_pos)

    res = []
    for i in range(len(graph)):
        global end_flag
        end_flag = False
        global circle_flag
        circle_flag = False
        dfs([i], i)
        if end_flag and not circle_flag:
            res.append(i)
    return res

def eventualSafeNodes(graph):
    terminal = []
    adjacent = defaultdict(list)
    for v, next in enumerate(graph):
        for pos in next:
            adjacent[v].append(pos)

    for v, next in enumerate(graph):
        if len(next) == 0:
            terminal.append(v)

    def dfs(v, visited, i):
        flag = True
        terminal_flag = False
        for next_pos in adjacent[v]:
            if visited[next_pos] >= 1:
                return False
            if next_pos in terminal:
                terminal_flag = True
            if not terminal_flag:
                visited[next_pos] += 1
                flag_now = dfs(next_pos, visited, i)
                flag &= flag_now
                if not flag:
                    return False
            else:
                terminal_flag = False
                for key in visited.keys():
                    if key >= next_pos:
                        visited[key] = 0
        return flag

    res = []
    for i in range(len(graph)):
        visited = defaultdict(int)
        visited[i] = 1
        safe_flag = dfs(i, visited, i)
        if safe_flag: res.append(i)
    return res

graph = [[],[0,2,3,4],[3],[4],[]]
print(eventualSafeNodes(graph))