# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        re_head = None

        while head:

            Node = ListNode(head.val)
            Node.next = re_head
            re_head = Node

            head = head.next

        return re_head