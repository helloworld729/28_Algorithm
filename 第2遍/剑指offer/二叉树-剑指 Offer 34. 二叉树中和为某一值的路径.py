class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """回溯递归， 问题化简"""
    def pathSum(self, root: TreeNode, target: int):
        if not root: return []

        def back(root, need):
            if root.left is None and root.right is None:
                if root.val == need: return [[need]]
                else: return []

            temp = []
            cans = [i for i in [root.left, root.right] if i]
            for node in cans:
                for data in back(node, need-root.val):
                    temp.append([root.val] + data)
            return temp

        res = back(root, target)  # 根节点, 需要的sum
        return res

    def pathSum2(self, root: TreeNode, target: int):
        # 已经有的节点和，将要探测的节点
        if not root: return []
        res = []

        def dfs(have, root, have_sum):
            # 边界条件，叶子结点
            if root.left is None and root.right is None:
                if have_sum + root.val == target:
                    res.append(have + [root.val])
                return
            if root.left:  dfs(have + [root.val], root.left,  have_sum + root.val)
            if root.right: dfs(have + [root.val], root.right, have_sum + root.val)

        dfs([], root, 0)
        return res

"""
纯回溯思维：
边界条件：当做是底层的子问题
递推函数：分解子问题
因为子问题不能重复利用，所以在二叉树类的题目中，可以使用而不用担心浪费时间。

dfs思维：
不断推进，遇到边界判定需不需要加入到外部全局变量中。
"""