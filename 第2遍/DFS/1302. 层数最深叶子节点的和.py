# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # 广度优先搜索
        if not root: return root
        que = deque()
        que.append(root)
        res = list()
        while que:
            res.clear()
            # print("*******************")
            for i in range(len(que)):
                root = que.popleft()
                # print(root.val)
                if root.left: que.append(root.left)  #
                if root.right: que.append(root.right)
                if not root.left and not root.right:  # 叶子节点
                    res.append(root)
        ret = 0
        for data in res:
            ret += data.val
        return ret

    def __init__(self):
        self.depth = -1
        self.res = 0

    def deepestLeavesSum2(self, root: TreeNode) -> int:
        """广度优先搜索，深度增加就重置"""
        def dfs(root, depth):
            if not root: return
            if depth > self.depth:
                self.depth, self.res = depth, root.val  # update
            elif depth == self.depth:
                self.res += root.val
            # print(root.val, self.res)

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)

        return self.res

