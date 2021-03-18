# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
# 思路：中序遍历 + 指针
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 中序遍历就是目标顺序，在遍历的过程中动态的连接

        # baseCase1
        if not root: return root

        cans = []  # 栈

        # 找到 头和尾，访问尾部触发停止条件
        head = root
        while head and head.left: head = head.left
        tail = root
        while tail and tail.right: tail = tail.right

        pre = tail

        # 中序遍历
        while cans or root:
            while root is not None:
                cans.append(root)
                root = root.left
            cur = cans.pop()  # 访问到本节点，说明左子树以及访问完毕了
            root = cur.right  # 接下来 开始访问右子树
            # 构建双向链表
            pre.right = cur
            cur.left = pre
            pre = cur
            if cur is tail: break

        return head




