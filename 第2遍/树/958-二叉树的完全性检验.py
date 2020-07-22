# #################### 958. 二叉树的完全性检验 ##############################
# 方法：利用完全二叉树的索引关系
"""给定一个二叉树，确定它是否是一个完全二叉树。"""
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        que = deque()
        que.append((0, root))
        count = 0
        while que:
            index, root = que.popleft()
            if index != count:
                return False

            if root.left: que.append((2 * index + 1, root.left))
            if root.right: que.append((2 * index + 2, root.right))

            count += 1

        return True