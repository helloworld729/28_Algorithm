# ############################## 104. 二叉树的最大深度 ###########################
"""
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
思路1：队列，每次弹出的次数为当前队列的长度
思路2：递归:高度=1+max(left, right)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        level, que = 0, deque()
        que.append(root)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return level

    def maxDepth_2(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        return 1 + max(self.maxDepth_2(root.left), self.maxDepth_2(root.right))


