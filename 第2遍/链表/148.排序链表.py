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
        def merge(head1, head2):
            p = q = ListNode(0)
            while head1 and head2:
                if head1.val < head2.val:
                    q.next = head1
                    q, head1 = q.next, head1.next
                else:
                    q.next = head2
                    q, head2 = q.next, head2.next

            q.next = head2 if not head1 else head1
            return p.next

        def getMid(head):
            fast, slow = head.next, head
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            fast = slow.next
            slow.next = None
            return head, fast

        if not head or not head.next: return head

        left, right = getMid(head)
        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)

a = ListNode(val=4, next=ListNode(val=2, next=ListNode(1, next=ListNode(5, None))))
res = Solution()
node = res.sortList(a)
while node:
    print(node.val, end=" ")
    node = node.next
