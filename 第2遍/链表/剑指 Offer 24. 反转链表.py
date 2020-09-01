class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def build(self, lst):
        head = p = ListNode(0)
        for d in lst:
            head.next = ListNode(d)
            head = head.next
        return p.next

    def print_link(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def reverseList(self, head: ListNode):
        re_head = None           # 反转后的头部
        while head:
            p = head             # 辅助变量
            head = head.next     # 原头后移
            p.next = re_head     # 反指
            re_head = p          # 反头后移
        # self.print_link(re_head)
        return re_head

    def palindrome(self, head:ListNode):
        """快慢指针+链表翻转"""
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next
        re_head = self.reverseList(slow)

        while head and re_head:
            if head.val != re_head.val:
                return False
            head = head.next
            re_head = re_head.next
        return True

    def merge(self, head1, head2):
        """蛇皮走位"""
        if not head1:return head2
        if not head2: return head1
        pre = res  = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                pre.next = head1
                head1 = head1.next
            else:
                pre.next = head2
                head2 = head2.next
            pre = pre.next

        pre.next = head1 if head1 else head2
        return res.next

    def sortList(self, head: ListNode) -> ListNode:
        """递归排序 空间复杂度O(logn栈帧)"""
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # cut

        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)
        while left and right:  # merge
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    def sortList2(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next


# a = Solution()
# head = a.build([1,1])
# a.print_link(head)
# re_head = a.reverseList(head)
# print(a.palindrome(re_head))

# a = Solution()
# head1 = a.build([-2,-2])
# head2 = a.build([-10,-1])
# res = a.merge(head1, head2)
# a.print_link(res)

a = Solution()
head1 = a.build([1,3,2,5,4,6,8,7,9,0])
head1 = a.sortList2(head1)
a.print_link(head1)  # 排序


"""
反转、回文、融合、归并排序
"""

