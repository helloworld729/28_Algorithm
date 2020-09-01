# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


"""
A和B两个链表长度可能不同，但是A+B和B+A的长度是相同的，！！！！！！！所以遍历A+B和遍历B+A一定是同时结束。
相交的话A和B会同时到达焦点，否则会同时到达尾部的None(！！所以换头的条件是节点为空，而不是节点没有后继)。
"""
