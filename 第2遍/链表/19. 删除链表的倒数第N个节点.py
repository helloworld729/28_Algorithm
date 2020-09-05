# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head  # 头部复制
        while n > 0:  # 距离拉开
            q = q.next
            n -= 1
        if not q: return head.next  # ！！！如果q已经为空，表示要删除的就是头结点

        while q.next is not None:  # 同步后移
            p = p.next
            q = q.next
        p.next = p.next.next
        return head

# 查询一遍就把结果输出
# 链表常用技术：快慢指针、双指针

