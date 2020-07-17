from collections import deque
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
# 思路 弗洛伊德全局最短路径算法

