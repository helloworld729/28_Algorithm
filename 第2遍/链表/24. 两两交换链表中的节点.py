# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        ph_back = ListNode(0)
        ph = ph_back
        h1, h2 = head, head.next

        while h1 and h2:
            h1.next = h2.next
            h2.next = h1
            ph.next = h2

            h1 = h1.next
            ph = ph.next.next
            if h2.next and h2.next.next and h2.next.next.next:
                h2 = h2.next.next.next
            else:
                break

        return ph_back.next


"""
题目：
给定 1->2->3->4, 你应该返回 2->1->4->3.
思路：三指针
0->1->2->3->4->5
ph p1 p2
其中ph刚开始是复制的伪头，然后再后续的遍历中，作为前置的节点
每次p1与p2交换后，ph需要连接靠前的节点。
"""
