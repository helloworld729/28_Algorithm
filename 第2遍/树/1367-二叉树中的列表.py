"""
给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 
head为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。
链接：https://leetcode-cn.com/problems/linked-list-in-binary-tree

思路：层次遍历+递归
边界条件：链表为空，子树为空或者值不行等
trick：递归推进的优雅描述
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSubPath(self, head, root) -> bool:
        def match(root, head):
            if head is None:
                return True
            if root is None or root.val != head.val:
                return False

            if (root.val == head.val) and (match(root.left, head.next) or match(root.right, head.next)):
                return True
            else:
                return False

        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if match(node, head):
                return True
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        return False

