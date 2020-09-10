"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
"""
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        res = []
        que = deque()
        while deque:
            tmp = deque()
            for _ in range(len(que)):
                node = que.popleft()
                if len(res) % 2: tmp.appendleft(node.val)   # 偶数层 -> 队列头部
                else: tmp.append(node.val)                  # 奇数层 -> 队列尾部
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(list(tmp))
        return res

"""
内外都是用队列,res的长度暗示了当前是遍历奇数或者偶数层，如果是奇数层，则从队列右侧压入，
否则从左侧压入,大循环完全不变，层的返回按照要求即可。
"""