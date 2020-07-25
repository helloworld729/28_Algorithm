"""
思路：递归解法：维护一个取值区间，只有满足才在原列表推进
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.index = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)

        def dfs(low, high):
            if self.index == n:
                return
            value = preorder[self.index]
            if value < low or value > high:
                return

            # 满足条件的值
            self.index += 1
            root = TreeNode(value)
            root.left = dfs(low, value)
            root.right = dfs(value, high)
            return root

        return dfs(float("-inf"), float("inf"))

    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        pass


