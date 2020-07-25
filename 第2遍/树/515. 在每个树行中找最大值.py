"""
您需要在二叉树的每一行中找到最大的值。
示例：
输入:
          1
         / \
        3   2
       / \   \
      5   3   9
输出: [1, 3, 9]
思路：while-for-层次遍历
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        que = deque()
        res = []
        que.append(root)
        while que:
            num = float("-inf")
            for i in range(len(que)):
                node = que.popleft()
                num = max(num, node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(num)
        return res