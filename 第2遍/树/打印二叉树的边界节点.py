(n, root) = list(map(int, input().split()))
adjacent = {}
color = -1
for i in range(n):
    (rt, l, r) = list(map(int, input().split()))
    adjacent[rt] = (l, r)

def get_left(root):
    res = []
    while root:
        (l, r) = adjacent[root]
        node = l if l else r
        if node:
            res.append(node)
            root = node
        else:
            adjacent[root] = (color, color)  #
            break
    return res

def get_right(root):
    res = []
    while root:
        (l, r) = adjacent[root]
        node = r if r else l
        if node:
            res.append(node)
            root = node
        else:
            adjacent[root] = (color, color)
            break
    return res

def get_leaf(root, adjacent):
    res = []
    def dfs(root):
        if adjacent[root] == (0, 0):
            res.append(root)
            return
        if adjacent[root] == (1, 1):
            return
        for n in adjacent[root]:
            if not(n == 0 or n == -1):
                dfs(n)
    dfs(root)
    return res

left = get_left(root)
right = get_right(root)
leaf = get_leaf(root, adjacent)

print([root] + left + leaf + right[::-1])

"""
测试样例：
16 1
1 2 3
2 0 4
4 7 8
7 0 0
8 0 11
11 13 14
13 0 0
14 0 0
3 5 6
5 9 10
10 0 0
9 12 0
12 15 16
15 0 0
16 0 0
6 0 0
https://www.nowcoder.com/practice/33b88978734c42b68699d0c7cef9b598?tpId=101&&tqId=33230&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking

求叶子节点的时候要深搜一下，边界节点直接查一下就行，如果是完全二叉树，可以根据索引关系。
"""