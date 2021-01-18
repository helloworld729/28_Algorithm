# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/17 13:22

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        while head:
            node = ListNode(head.val)
            node.next = p.next
            p.next = node
            head = head.next
        return p.next

# 是一个逆生长的过程

