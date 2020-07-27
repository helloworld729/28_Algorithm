"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表
（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。 

输入：[1,2,3,4,5,null,7,8]
        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import deque


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree: return []
        res, que = [], deque()  # 答案容器, 层次遍历容器
        que.append(tree)

        while que:
            p = list_root = ListNode(0)
            for i in range(len(que)):
                node = que.popleft()
                list_root.next = ListNode(node.val)
                list_root = list_root.next

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(p.next)
        return res



