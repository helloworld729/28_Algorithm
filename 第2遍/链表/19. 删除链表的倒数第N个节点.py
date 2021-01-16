# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head

        # 思路：拉开距离 --> 一起移动
        left = right = head
        for i in range(n):
            right = right.next
        if not right:  # 如果right直接越界的话，说明要删头结点
            return head.next

        while right and right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head

# 查询一遍就把结果输出
# 链表常用技术：快慢指针、双指针

