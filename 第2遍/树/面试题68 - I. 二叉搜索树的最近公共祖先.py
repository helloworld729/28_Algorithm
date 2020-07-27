# 结合搜索树的特点(左小右大)找到分叉点
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val: # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > p.val and root.val > q.val: # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else: break
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode-cn.com/problems/first-common-ancestor-lcci/
        # 适用于所有二叉树，
        if(not root or root == p or root == q):  # 能够到这里，说明前面都没有碰到p/q,当前节点又和其中一个相等，则
            return root                          # 该节点就是最近的公共祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root  # 左右子树分别找到了一个，说明节点就是祖先
        return left if left else right  # 只在一侧(当然可能在子树的两侧)
