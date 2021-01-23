# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/17 12:52

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = q = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                q.next = l1
                l1 = l1.next
                q = q.next
            else:
                q.next = l2
                l2 = l2.next
                q = q.next
        if not l1:
            q.next = l2
        else:
            q.next = l1
        return p.next

# 走位方式：先设置两个伪头部

