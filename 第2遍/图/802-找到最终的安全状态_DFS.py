from collections import defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        def dfs(node):
            # 如果一个节点不是第一次访问，只有黑色节点会返回True
            # 表示该节点是一个安全节点
            if color[node] != WHITE:
                return color[node] == BLACK
            # 能到这里表名该节点被首次访问，染为灰色
            color[node] = GRAY
            for nei in graph[node]:
                # 由于后继可能有多个，一个后继为黑色不能保证节点安全
                if color[nei] == BLACK:
                    continue
                # 但是若后继已被访问或者不安全，该节点必不安全
                if color[nei] == GRAY or not dfs(nei):
                    return False
            # 能到这里，说明所有后继都是安全节点，该节点则安全
            color[node] = BLACK
            return True

        return list(filter(dfs, range(len(graph))))

# 可以看出，算法始终对全局节点染色，无需使用全局变量、深度拷贝等等
# 我们的目的不是输出安全路径，只要标记安全节点。
# 深度优先搜索的思路：
# trick：染色的思想
# 一个节点是不是安全取决于其后继是否安全，假如所有安全则安全
# 只要有一个后继不安全，就不安全。
# is_safe(A)= is_safe(A1)& is_safe(A2)& is_safe(A3)
def dfs(s):  # 框架
    for i in next(s):
        if dfs(i):
            continue
        else:
            return False
    return True

# 错误解法：多dfs的介入太深，假如使用全局flag、deepcopy等


