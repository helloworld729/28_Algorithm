# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head
        head2 = head
        count = 0
        # 统计长度
        while head2:
            count += 1
            head2 = head2.next
        k = k % count
        if k == 0: return head  # !!!

        # 求倒数第k个节点
        h1, h2 = head, head
        for i in range(k):
            h2 = h2.next
        while h1.next and h2.next:
            h1 = h1.next
            h2 = h2.next

        rest_head1,  rest_head2 = h1.next, h1.next  # 剩余部分的头部
        h1.next = None  # cut
        while rest_head1 and rest_head1.next:
            rest_head1 = rest_head1.next
        rest_head1.next = head

        return rest_head2


"""
思路：求出链表长度->计算有效K->求倒数第k个节点的前一节点(记作h1)，并基于该节点求出剩余部分的头部
      原链表在h1处阶段，并拼接在剩余部分的后面
"""

