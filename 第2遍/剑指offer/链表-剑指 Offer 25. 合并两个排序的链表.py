# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        p = re_head = ListNode(0)  # 伪头

        while l1 and l2:
            v1, v2 = l1.val, l2.val
            if v1 < v2:
                new_val = v1
                l1 = l1.next
            else:
                new_val = v2
                l2 = l2.next
            node = ListNode(new_val)
            re_head.next = node
            re_head = re_head.next

        re_head.next = l1 if l1 else l2  # 余项

        return p.next
