class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def getClonedNode(node):
            if node is not None:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return None

        if not head: return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        # 构建一个哈希表，key为旧链表的节点，value为新链表的节点
        # 模仿key之间的连接关系，构建value之间的连接关系。
        visited[old_node] = new_node

        while old_node:
            # 如果old_node的相关后继不在哈希表中，就移到hash表中
            # 并且构建一个只有val的copy，在后续不断的添加next和random
            new_node.random = getClonedNode(old_node.random)
            new_node.next   = getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return visited[head]

    def copyRandomList2(self, head: 'Node') -> 'Node':
        if not head: return head
        # 链表 拷贝 与 嵌入
        # random定向
        # 链表分离

        # 链表拷贝
        head1 = head
        while head1:
            node = Node(head1.val)  # value copy
            node.next = head1.next  # next copy
            head1.next = node  # 向后连接
            head1 = node.next  # 向前连接

        # random 定向
        head1 = head
        while head1 and head1.next:
            head1.next.random = head1.random.next \
                if head1.random else None
            head1 = head1.next.next

        # 链表分离
        copyHead1, copyHead2 = head.next, head.next
        while copyHead1 and copyHead1.next:
            copyHead1.next = copyHead1.next.next
            copyHead1 = copyHead1.next

        return copyHead2


