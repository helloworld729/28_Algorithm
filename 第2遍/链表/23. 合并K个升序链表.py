class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # 初始化
        ll = len(lists)
        sub = []
        for i in range(ll):
            if lists[i]: sub.append((lists[i]))
        sub.sort(key=lambda x: x.val, reverse=True)
        p = head = ListNode(0)

        def half_search(sub, cans):
            l, r = 0, len(sub)
            while l < r:
                middle = l + (r-l) // 2
                if cans.val < sub[middle].val: l = middle + 1
                else:r = middle
            return l

        while sub:
            node = sub.pop()  # 节点值
            head.next = ListNode(node.val)
            head = head.next

            if not node.next: continue
            cans = node.next
            if sub and cans.val <= sub[-1].val:
                sub.append(cans)
            else:  # 二分插入
                pos = half_search(sub, cans)
                sub.insert(pos, cans)
        return p.next

# 复杂度分析
# 时间复杂度：假设k个链表， n个节点，每个节点入栈一次，出栈一次，复杂度为O(N)
# 每次查询时消耗logK的复杂度，列表的插入是K的复杂度，所以时间复杂度为O(KN)
# 空间复杂度 O(K)
