"""
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def parent(root, root_parent=None):  # 反向路径构建
            if not root: return
            root.parent = root_parent
            parent(root.left, root)
            parent(root.right, root)
            return root
        root = parent(root)

        def back(root):  # 回溯函数
            res = []
            while root is not None:
                res.append(root.val)
                root = root.parent
            self.res.append(res[::-1])

        def dfs(root, current_sum):
            if root is None: return
            if current_sum + root.val == sum and root.left is None and root.right is None:  # 是叶子节点
                back(root)  # 满足条件，回溯
            for child in [root.left, root.right]:
                dfs(child, current_sum+root.val)
        dfs(root, 0)
        return self.res
    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 拷贝
        def dfs(root, current_ele, current_sum):
            if root is None: return
            if current_sum + root.val == sum and root.left is None and root.right is None:  # 是叶子节点
                self.res.append(current_ele+[root.val])
            for child in [root.left, root.right]:
                dfs(child, current_ele+[root.val], current_sum+root.val)
        dfs(root, [], 0)
        return self.res
