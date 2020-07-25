# ########################## 111. 二叉树的最小深度 #############################
"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
思路：层次遍历，当没有后继的时候，说明达到了最近的叶子节点
陷阱：通过判断节点本身为空，返回index-1， 会导致[1， 2]这种树的深度为1，实际为2
树高：深度必须有叶子节点，除非单节点树
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        que = deque()
        que.append((root, 1))
        while que:
            node, index = que.popleft()
            left, right = node.left, node.right
            if left is None and right is None:
                return index
            if left: que.append((left, index + 1))
            if right: que.append((right, index + 1))
