# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/7 10:21

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 找到中间节点
        # 归并算法

        def getMidPoint(head: ListNode):
            # 快慢指针 获取中间节点
            if not head: return None
            slow, fast = head, head.next  # 慢指针在前
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None
            return mid

        def merge(formmer, latter):
            node = ListNode(0)
            res = node
            while formmer or latter:
                if formmer and latter:
                    if formmer.val > latter.val: node.next, latter = latter, latter.next
                    else: node.next, formmer = formmer, formmer.next
                    node, node.next = node.next, None
                else:
                    node.next = formmer if formmer else latter
                    break
            return res.next

        if not head or not head.next: return head

        latter = getMidPoint(head)
        formmer, latter = self.sortList(head), self.sortList(latter)
        node = merge(formmer, latter)

        return node

a = ListNode(val=4, next=ListNode(val=2, next=ListNode(1, next=ListNode(5, None))))
res = Solution()
node = res.sortList(a)
while node:
    print(node.val, end=" ")
    node = node.next
