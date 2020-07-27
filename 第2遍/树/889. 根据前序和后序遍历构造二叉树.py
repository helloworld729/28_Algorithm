"""
889. 根据前序和后序遍历构造二叉树
返回与给定的前序和后序遍历匹配的任何二叉树。
 pre 和 post 遍历中的值是不同的正整数。
输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
思路：左子树在先序的index(1)，结合后续可以切出左子树和右子树
改进：用索引代替列表切片(浅拷贝)
提示：
1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return None
        root = TreeNode(pre[0])

        # if len(pre) == 1 and pre[0] == "null": return None  # 只有数字
        if len(pre) == 1: return root
        if len(pre) == 2:  # 非必须，但是可以加速
            left = TreeNode(pre[1])
            root.left = left
            return root

        left_len = post.index(pre[1]) + 1  # 左子树长度
        left_pre = pre[1: left_len + 1]    # 左子树先序
        left_post = post[0: left_len]      # 左子树后序
        right_pre = pre[left_len + 1:]     # 右子树先序
        right_post = post[left_len: -1]    # 右子树后续

        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)
        return root