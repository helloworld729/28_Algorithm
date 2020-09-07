from collections import defaultdict
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

tickets =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res = findItinerary(tickets)
print(res)

"""
思路：先把后继节点入栈，再把当前节点入栈，为什么要这样呢？因为我们不知道从当前节点
出发，哪一条路径可以构成欧拉通路， 当然可以通过普通的dfs暴力搜索，但会超时，换一个
原点：入度<出度
终点：入度>出度
其他：入度=出度

当我们从该节点出发，如果一条分支不会达到终点，那么最终还是会回到该节点
如果一条分支可以到达终点，就没有回来的路径，所以可以这样：
后继节点先入栈，当前节点再入栈，结果再反过来。

特点：走过的路径要删掉，这样不会导致路径回不来，是为了避免死循环
对于本题而言会先对路径排序。此方法可以求条件最优值，无法求所有路径。

Hierholzer 算法用于在连通图中 逆序入栈 寻找欧拉路径
"""