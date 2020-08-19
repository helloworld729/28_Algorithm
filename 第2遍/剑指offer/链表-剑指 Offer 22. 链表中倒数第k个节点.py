# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head, k: int):
        if not head: return head
        h = head
        ll = 0
        # 统计长度
        while head:
            ll += 1
            head = head.next

        # 找到第k个节点
        count = 0
        p = None
        while h and count < ll-k+1:
            count += 1
            p = h
            h = h.next
            # print(count, p.val)
        return p

    def getKthFromEnd2(self, head, k: int):
        """方法2：双指针"""
        if not head: return head
        l, r = head, head
        while k > 0:
            r = r.next
            k -= 1
        while r:
            l, r = l.next, r.next
        return l