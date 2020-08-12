"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意
节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
方法1：dfs只有左右子树都是平衡二叉树，并且深度差小于等于1，返回True
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root, level):
            (deep_l, flag1) = dfs(root.left, level + 1) if root.left else (level, True)
            (deep_r, flag2) = dfs(root.right, level + 1) if root.right else (level, True)
            if flag1 and flag2 and abs(deep_l - deep_r) <= 1:
                return (max(deep_r, deep_l), True)
            else:
                return (0, False)
        if not root or dfs(root, 0)[1]: return True
        return False

