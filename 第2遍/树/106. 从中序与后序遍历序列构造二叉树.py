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
from collections import deque
def serialize(root):
    if not root: return "[]"
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")

    while res[-1] == "null":
        res.pop()

    return '[' + ','.join(res) + ']'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not postorder: return None  # 必备边界条件
        root_val = postorder[-1]
        root = TreeNode(root_val)
        # 求根节点的索引
        cut = inorder.index(root_val)

        in_left  = inorder[:cut]
        # 可能越界，但是列表切片不会报错，会返回空表，所以不用担心
        in_right = inorder[cut+1:]
        # 中序左子树的长度适用于右子树
        post_left  = postorder[:cut]
        post_right = postorder[cut:-1]

        root.left  = self.buildTree(in_left,  post_left)
        root.right = self.buildTree(in_right, post_right)

        return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
a = Solution()
root = a.buildTree(inorder, postorder)
res = serialize(root)
print(res)



"""
边界条件：1、判空 例如根节点为1，只有一个左后继为2，此时右树为空
边界条件：2、单点树可以不用判断，但是如果判断可以加速
"""


