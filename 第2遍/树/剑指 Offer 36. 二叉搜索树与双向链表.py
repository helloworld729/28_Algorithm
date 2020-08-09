"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。

方法：中序遍历
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        first = current = None
        st = []
        while st or root:
            while root:
                st.append(root)
                root = root.left
            node = st.pop()
            if not first:
                first = current = node
            else:
                current.right = node
                node.left = current
                current = node
            root = node.right

        current.right = first
        first.left = current

        return first

