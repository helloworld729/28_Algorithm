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
        """链表拷贝-->random定向-->链表分离"""
        if not head: return head
        h1 = head

        # 链表拷贝
        while h1:
            copy = Node(h1.val)
            copy.next = h1.next
            h1.next = copy
            h1 = h1.next.next
        new_head = head.next
        h2 = head
        new_head2 = new_head

        # random定向
        while h2:
            if h2.random:
                new_head2.random = h2.random.next
            h2 = h2.next.next
            if h2 and h2.next:
                new_head2 = h2.next

        # 链表分离
        new_head3 = new_head
        while new_head3:
            if new_head3.next:
                new_head3.next = new_head3.next.next
            new_head3 = new_head3.next
        return new_head


