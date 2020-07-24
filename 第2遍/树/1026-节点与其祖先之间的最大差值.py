# ##################################### 节点与祖先之间的最大差值 ##############################
"""
给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 
V = |A.val - B.val|，且 A 是 B 的祖先。（如果 A 的任何子节点之一为 B，
或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
链接：https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor
注意：关键是在队列/栈中存储（本节点，最大的祖先节点值，最小的祖先结点值）
      不要初始化为0，而是root的值，否则可能根节点和0的差值最大。
      队列和栈都可以用的时候，优先使用栈。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        que = deque()
        res = 0  # 最大差值
        que.append((root, root.val, root.val))  # 当前节点，最大祖先值，最小祖先值
        while que:
            # print(res, end=" ")
            root, max_num, min_num = que.popleft()
            value = root.val
            res = max(res, abs(max_num - value), abs(value - min_num))
            max_num, min_num = max(max_num, value), min(min_num, value)
            if root.left: que.append((root.left, max_num, min_num))
            if root.right: que.append((root.right, max_num, min_num))
        return res
