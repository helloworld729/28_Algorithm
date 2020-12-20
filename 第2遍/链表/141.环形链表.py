class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        slow, fast = head, head.next.next
        while slow and fast:
            if slow == fast:
                return True
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else: break
        return False

"""
链表环路检测：用快慢指针的方法：为什么可以用快慢指针呢？假如链表有环的话，那么两个指针都会进入到
环路中，而后假设快慢没有对齐，则有一定的间隔，设为K，由于快指针每次比满指针多运行一格，那么下一次
的苦力是k-1，最后总会相遇，就像一个人在前面静止，而另一个人匀速运动，两个人肯定会相遇。
"""