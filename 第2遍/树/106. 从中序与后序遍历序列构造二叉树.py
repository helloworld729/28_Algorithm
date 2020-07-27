"""
根据一棵树的中序遍历与后序遍历构造二叉树。
你可以假设树中没有重复的元素。
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
思路：
1、求出根节点在中序的索引，切分为左右子树的中序
2、从中序中求出右子树的长度
3、根据右子树的长度从后序中切分处左右子树的后序
4、递归
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder: return None
        root = TreeNode(postorder[-1])
        if len(postorder) == 1: return root

        root_index = inorder.index(postorder[-1])  # 根节点在中序的索引
        right_len = len(inorder)-root_index-1  # 右子树的长度

        left_in = inorder[: root_index]
        right_in = inorder[root_index: ]
        left_post = postorder[:-1-right_len]
        right_post = postorder[-1-right_len: -1]

        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)

        return root

