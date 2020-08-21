# ################ 剑指 Offer 37. 序列化二叉树 ##############################
# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/submissions/
# 小结：对序列化列表分割首选re.sub，因为可以针对,和[]分割，注意首尾为空
# index规则，null_mem。
import re
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")

        while res[-1] == "null":
            res.pop()

        return '[' + ','.join(res) + ']'

    def deserialize(self, data):  # str到root
        if data == "[]":
            return []
        null_count = 0
        # data = re.split(r" |,|\[|\]", data)
        data = data[1:-1].split(",")
        def to_node(num): return "null" if num == "null" else TreeNode(int(num))
        node_list = list(map(to_node, data))
        ll = len(node_list)
        que = deque()
        root, index = node_list[0], 1
        que.append(root)

        while que:
            # 无论是否为null，都会推进index
            # 只有非空，才会加到根节点队列中
            node = que.popleft()
            if index <= ll - 1:
                left = node_list[index]
                if left != "null":
                    node.left = left
                    que.append(left)

            index += 1
            if index <= ll - 1:
                right = node_list[index]
                if right != "null":
                    node.right  = right
                    que.append(right)
            index += 1

        return root


lst = "[1,2,3,null,null,4,5,6,7]"
a = Codec()
root = a.deserialize(lst)
print(a.serialize(root))

"""
思路：序列化很简单，就是一个层次遍历，逆序列化的时候维护一个根节点的队列，
      和当前索引位置的指针。指针指向的位置就是当前弹出根节点的后继。


lst = "[1,2,3,null,null,4,5,6,7]"
约定：提供的lst中不是所有的节点信息，假如一个节点是null，那么后续就没有它的信息了
      所以逆序列化的时候，null没有进入队列，序列化的时候，也是直接加入一个null、
实例：67节点是4的后继，但是6之前不会列出4个null，这是leetcode的约定做法。

lst = "[1,2,3,null,null,4,5,null,nul,null,nul,6,7]"
问题：为什么不用完全信息呢？
假如用了完全信息，在序列化的时候，我们遇到了节点为None的情况怎么处理呢?
如果只是把null加入到res中，但是不会加入到队列中，这样序列化就和lst不对应
如果不仅把null加入到res中，而且还会加入到队列中，那么循环就停不下来了。
综上：空节点的后继不会出现在序列化的结果中。
"""

