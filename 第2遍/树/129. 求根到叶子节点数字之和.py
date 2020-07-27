"""
129. 求根到叶子节点数字之和
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。
思路：广度优先
示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        total_sum, que = 0, deque()
        que.append(("0", root))  # 先驱的和, 本节点

        while que:
            pre_num, root = que.popleft()
            current_num = pre_num + str(root.val)
            if root.left: que.append((current_num, root.left))  # 注意不要用elif，因为可能是两个子节点
            if root.right: que.append((current_num, root.right))
            if not root.left and not root.right: total_sum += int(current_num)

        return total_sum
