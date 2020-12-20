# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2020/11/24 10:12

# 直接递归、层次遍历、深度优先遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def countNodes1(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + self.countNodes1(root.left) + self.countNodes1(root.right)

    # 层次遍历
    def countNodes2(self, root: TreeNode) -> int:
        if not root: return 0
        counts = 0
        st = [root]
        while st:
            node = st.pop()
            counts += 1
            if node.left: st.append(node.left)
            if node.right:st.append(node.right)
        return counts

    # 迭代法
    def countNodes(self, root: TreeNode) -> int:
        count, st = 0, []
        st.append(root)
        while st:  # st是一个容器
            root = st.pop()
            while root is not None:
                count += 1
                st.append(root.right)
                root = root.left
        return count
