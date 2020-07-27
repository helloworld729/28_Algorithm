"""
给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。

如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个
节点都在以 A 为根节点的子树中，且A的深度达到此条件下可能的最大值。

输入：root = [1,2,3]
输出：[1,2,3]
解释：
最深的叶子是值为 2 和 3 的节点。
这些叶子的最近共同祖先是值为 1 的节点。
返回的答案为序列化的 TreeNode 对象（不是数组）"[1,2,3]" 。
思路：
1、假如左右子树的最大深度相等，返回本节点
2、假如左子树较深，返回 左分支回溯的节点
3、假如右子树较深，返回 有分支回溯的节点
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def max_deep(level, root):  # 先驱深度，本节点
            if not root: return (0, None)
            (deep_l, left) = max_deep(level+1, root.left) if root.left else (level, root)
            (deep_r, right) = max_deep(level+1, root.right) if root.right else (level, root)
            if deep_l == deep_r: return (deep_l, root)
            if deep_l > deep_r:return (deep_l, left)
            else: return (deep_r, right)
        return max_deep(0, root)[1]