"""
1372. 二叉树中的最长交错路径
方向每变化一次，路径长度就加1
https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.length = 0
    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(root, pre, length):  # 当前节点，前一节点方向， 已经长度
            if not root:
                return
            self.length = max(self.length, length)
            if pre == 0 or length == 0:  # 左
                dfs(root.left, 0, 1)
                dfs(root.right, 1, length+1)
            else:
                dfs(root.left, 0, length+1)
                dfs(root.right, 1, 1)
        if not root: return 0
        dfs(root, 0, 0)
        return self.length