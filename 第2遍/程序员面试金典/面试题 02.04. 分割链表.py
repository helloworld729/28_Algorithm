# 题目：小于x的放到左边，顺序不做要求,即partition操作
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 保证p指针以及p指针左边的是小值
        p, q = head, head
        while q:
            if q.val < x:
                q.val, p.val = p.val, q.val
                p = p.next
            q = q.next
        return head

    def partition2(self, head: ListNode, x: int) -> ListNode:
        if not head: return head
        p_head = ListNode(float("-inf"))
        p_head.next = head
        l = r = p_head  # 明确左指针位置
        while r.val < x: r = r.next  # 明确右指针位置

        # 如果有指针没有后继说明右侧不再需要partition
        while r and r.next:
            # 后继为空或者遇到逆序
            while l.next and l.next.val < x:
                l = l.next
            # 后继为空或者遇到顺序
            while r.next and r.next.val >= x:
                r = r.next
            if not r or not r.next: break

            # 节点交换
            back = r.next.val  # 右值备份
            temp = ListNode(l.next.val)
            temp.next = r.next.next
            r.next = temp
            templ = ListNode(back)
            templ.next = l.next.next
            l.next = templ

            l = l.next
            r = r.next

        return p_head.next
