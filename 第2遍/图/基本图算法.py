class GraphError(ValueError):
    pass
class Graph():
    def __init__(self, mat, unconn=0):
        self._vnum = len(mat)
        for row in mat:
            if len(row) != self._vnum:
                raise GraphError
        self._mat = mat
        self._unconn = unconn

    def vertex_num(self):
        return self._vnum

    def is_not_valid(self, v):
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        raise GraphError("not support now")

    def add_edge(self, vi, vj, val=1):  # 增
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("vi or vj is not valid")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):  # 查
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("vi or vj is not valid")
        return self._mat[vi][vj]

    def out_edges(self, vi):  # 返回节点对应的边信息
        if self.is_not_valid(vi):
            raise GraphError("vi is not valid")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn=0):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges


class GrapgAL(Graph):
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for row in mat:
            if len(row) != vnum:
                raise GraphError("不是方阵")
        self._mat = [self._out_edges(mat[i], 0) for i in range(vnum)]  # 二维列表，不是矩阵
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("节点非法")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if vj == row[i][0]:
                self._mat[vi][i] = (vj, val)  # i 是邻接边的在边表索引，不是邻接点的序号
                return
            # if vj < i:  # TODO
            #     break
            if vj < row[i][0]:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        """获取两个节点之间边信息"""
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("invalid")
        for con_info in self._mat[vi]:
            if con_info[0] == vj:
                return con_info[1]
        return self._unconn

    def out_edges(self, vi):
        """返回能结点的所有关联边"""
        if self.is_not_valid(vi):
            raise GraphError("结点非法")
        return self._mat[vi]

    def DFS_recur(self, v):
        """深度优先遍历"""
        color = 1
        visited = {i:0 for i in range(self._vnum)}
        res = []
        def dfs(v):
            # boundary
            if visited[v] == color: return
            visited[v] = 1
            res.append(v)
            if len(res) == self._vnum: return
            # go
            for (n, w) in self.out_edges(v):
                dfs(n)
        dfs(v)
        return res

    def dfs_nocur(self, v):
        """为了进行深度优先，可以将边表，当前需要访问边表的第几个元素压栈"""
        edges = self.out_edges(v)
        st = [(0, edges)]
        res = [v]
        visited = {i:0 for i in range(self._vnum)}
        visited[v] = 1
        while st:
            if len(res) == self._vnum:break
            i, edges = st.pop()
            if i+1 <= len(edges)-1: st.append((i+1, edges))
            n = edges[i][0]
            if not visited[n]:
                visited[n] = 1
                res.append(n)
                st.append((0, self.out_edges(n)))
        return res

    def bfs(self, v):
        from collections import deque
        que = deque()
        que.append(v)
        res = []
        visited = {i: 0 for i in range(self._vnum)}
        while que and len(res) != self._vnum:
            n = que.popleft()
            if not visited[n]:
                visited[n] = 1
                res.append(n)
                edges = self.out_edges(n)
                for (v, w) in edges:
                    que.append(v)
        return res

    def prim(self, v):
        mst = [None for _ in range(self._vnum)]  # 联通区
        cans = [(0, v, v)]  # 非联通区候选值
        count = 0
        while cans and count < self._vnum:
            w, vi, vj = cans.pop()  # 最优联通边
            if mst[vj]: continue    # 已经在联通区的话
            count += 1
            mst[vj] = ((vi, vj), w)
            for (vk, vk_weight) in self.out_edges(vj):
                if not mst[vk]:
                    cans.append((vk_weight, vj, vk))
            cans.sort(reverse=True)
        mst.sort()
        return mst

    def kruskal(self):
        mst, edges = [], []
        rep = [i for i in range(self._vnum)]  # representation
        for vi in range(self._vnum):  # all point
            vj_info = self.out_edges(vi)
            for vj, wj in vj_info:
                edges.append((wj, vi, vj))
        edges.sort()

        for weight, vi, vj in edges:
            if rep[vi] != rep[vj]:
                mst.append(((vi, vj), weight))
                if len(mst) == self._vnum:break
                srep, trep = rep[vi], rep[vj]
                for i in range(len(rep)):
                    if rep[i] == srep:
                        rep[i] = trep
        return mst

    def dijkstra(self, v0):
        """所有节点到单源点的最短路径"""
        path = [None for i in range(self._vnum)]  # link region
        cans = [(0, v0, v0)]  # candidata not link region
        count = 0
        while count < self._vnum and cans:
            w, vi, vj = cans.pop()
            if path[vj]: continue
            path[vj] = ((vi, vj), w)
            for vk, wk in self.out_edges(vj):
                if not path[vk]:
                    cans.append((w+wk, vj, vk))
            cans.sort(reverse=True)
        path.sort(key=lambda x:x[0][0])  # pre node
        return path

    def topo_sort(self):
        """深度优先"""
        zero_v = -1
        in_degree, topsort = [0 for i in range(self._vnum)], []

        for v in range(self._vnum):
            for vj, w in self.out_edges(v):
                in_degree[vj] += 1
        for v in range(self._vnum):
            if in_degree[v] == 0:
                in_degree[v] = zero_v
                zero_v = v

        while zero_v != -1:
            vi = zero_v  # 当前零度指针
            zero_v = in_degree[zero_v]  # 更新0度指针
            topsort.append(vi)
            for vj, w in self.out_edges(vi):
                in_degree[vj] -= 1
                if in_degree[vj] == 0:
                    in_degree[vj] = zero_v
                    zero_v = vj
        return topsort

    def top_sort_bfs(self):
        """广度优先"""
        from collections import deque
        zero_v = deque()
        in_degree, topsort = [0 for i in range(self._vnum)], []

        for v in range(self._vnum):
            for vj, w in self.out_edges(v):
                in_degree[vj] += 1

        for v in range(self._vnum):
            if in_degree[v] == 0:
                zero_v.append(v)

        while zero_v:
            zero = zero_v.popleft()
            topsort.append(zero)
            for vj, w in self.out_edges(zero):
                in_degree[vj] -= 1
                if in_degree[vj] == 0:
                    zero_v.append(vj)
        return topsort

# mat = [
#     [0, 10, 1, 0, 1, 0],  # 1 2 4
#     [10, 0, 0, 1, 1, 0],  # 0 3 4
#     [1, 0, 0, 0, 1, 1],   # 0 4 5
#     [0, 1, 0, 0, 0, 0],   # 1
#     [1, 1, 1, 0, 0, 0],   # 0 1 2
#     [0, 0, 1, 0, 0, 0],   # 2
# ]

mat = [
    [0, 1, 1, 0, 1, 0],  # 0-：1 2 4
    [0, 0, 0, 1, 1, 0],  # 1-：3 4
    [0, 0, 0, 0, 1, 1],  # 2-：4 5
    [0, 0, 0, 0, 0, 0],  #
    [0, 0, 0, 0, 0, 0],  #
    [0, 0, 0, 0, 0, 0],  #
]

graph = GrapgAL(mat)
print(graph.dijkstra(0))

"""
1、图遍历：基于递归或者迭代
2、最小生成树：两种方法 K算法和P算法
3、最短路径：D算法
4、拓扑排序

深度优先遍历：为了简答起见，可以无条件递归，在边界条件中处理是否要立即返回
还有就是，如果在函数中定义了子函数，那么一定要调用

最小生成树：Kruskal、prim

Kruskal算法思想：代表元初始化->边表统计->部落扩展以及代表切换
拓扑排序：可以用栈、链表进行深度优先，后者使用队列广度优先

prim算法思想：划分为联通区和非联通区

最短路径：Dijkstra，划分为联通区和非联通区，每次选择最佳通道
什么是联通区呢？首先初始化path(前一节点、后一节点，到原点的长度)，为None，每增加
节点就会写入到path中，知道终止。

"""
