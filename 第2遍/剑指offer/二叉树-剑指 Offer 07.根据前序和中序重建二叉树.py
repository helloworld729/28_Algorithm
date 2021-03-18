# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前序：根 左 右
# 中序：左 根 右
# 基于中序遍历-->可以得到左右子树的中序遍历
# 然后测量左子树的元素个数，从前序中切分出左右子树的前序遍历
# keyPoint:测量宽度

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1: return root

        rootIndex = inorder.index(preorder[0])  # 根节点的索引 也是左子树的长度
        preLeft = preorder[1: 1 + rootIndex]  # 左子树 前序遍历
        preRight = preorder[1 + rootIndex:]  # 右子树 前序遍历
        midLeft = inorder[:rootIndex]
        midRight = inorder[1 + rootIndex:]
        root.left = self.buildTree(preLeft, midLeft)
        root.right = self.buildTree(preRight, midRight)

        return root
