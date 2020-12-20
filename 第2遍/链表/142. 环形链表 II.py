class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            # while 循环检测是否有环
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            # 快慢指针相遇，说明有环，跳出
            if fast == slow: break
        # 求入环节点
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


"""
求环路的开始节点：由推算后得知，求入口节点可以分为两步：
1、快慢指针相遇在节点b
2、从节点b和head节点开始 使用连个指针，再次相遇就是环路的入口节点

有一个值得注意的地方就是刚开始的时候快慢指针均指向头部，然后按照如下的方式：
先移动 再判断
"""
