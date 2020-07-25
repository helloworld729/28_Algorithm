# #################################### 863. 二叉树中所有距离为 K 的结点 #####################
"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/
思路：# 边表统计+dfs+染色(visited)
"""

from collections import defaultdict
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adjacent = defaultdict(list)
        st = [root]
        while st:  # 边表统计
            root = st.pop()
            value = root.val
            if root.left:
                st.append(root.left)
                adjacent[value].append(root.left.val)
                adjacent[root.left.val].append(value)
            if root.right:
                st.append(root.right)
                adjacent[value].append(root.right.val)
                adjacent[root.right.val].append(value)
        # print(adjacent)
        visited = {target.val: 1}  # 染色

        def dfs(vi, k):  # 深度优先遍历
            if k == 0:
                self.res.append(vi)
                return
            for vj in adjacent[vi]:
                if visited.get(vj, 0) == 0:
                    visited[vj] = 1
                    dfs(vj, k - 1)

        dfs(target.val, K)
        return self.res

    def distanceK2(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        que = deque()
        visited = {target.val: 1}
        que.append((target, 0))
        while que:
            root, index = que.popleft()
            if index == K:
                return [root.val] + [node.val for node, index in que]
            for node in [root.left, root.right, root.parent]:
                if node and node.val not in visited:
                    que.append((node, index+1))
                    visited[node.val] = 1
        return []

    def distanceK3(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        que = deque()
        visited = {target.val:1}
        que.append((target, 0))
        while que:  # why
            for i in range(len(que)):
                root, index = que.popleft()
                # print(index)
                if index == K:
                    return [root.val]+[node.val for node, _ in que]
                for node in [root.left, root.right, root.parent]:
                    if node and (node.val not in visited):
                        # print(node.val, end=" ")
                        que.append((node, index+1))
                        visited[node.val] = 1
        return []




