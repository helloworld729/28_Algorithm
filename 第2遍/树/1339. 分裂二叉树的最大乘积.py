"""
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树
分裂成两棵子树，且它们子树和的乘积尽可能大。
由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。
输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
链接：https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree
思路：求所有的子树和(顺便得到总的和)-->找到最接近一半总值的子树和
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self,):
        self.total_sum = 0  # 总和
        self.child_sum = []
    def maxProduct(self, root: TreeNode) -> int:
        # 计算子树和
        def child_sum(root):
            if not root: return 0
            left = child_sum(root.left) if root.left else 0
            right = child_sum(root.right) if root.right else 0
            self.child_sum.append(left+right+root.val)
            return left + right + root.val
        child_sum(root)
        self.total_sum = self.child_sum[-1]

        best, diff =0, float("inf")
        for data in self.child_sum:
            distance = abs(data * 2 -self.total_sum)
            if distance < diff:
                best = data
                diff = distance
        return (best * (self.total_sum-best)) % (pow(10,9)+7)