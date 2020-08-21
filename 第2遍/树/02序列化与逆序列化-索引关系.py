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
    def serialize(self, root):  # root-->str
        if not root:
            return "[]"
        # 返回值，处理队列
        res, que = [], deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else: res.append("null")

        while res[-1] == "null":
            res.pop()

        res = "[" + ",".join(res) + "]"
        return res

    def deserialize(self, data):  # str到root
        if data == "[]":  return []
        null_count = 0
        data = data[1:-1].split(",")

        def to_node(num): return "null" if num == "null" else TreeNode(int(num))
        node_list = list(map(to_node, data))

        for index, node in enumerate(node_list):
            if node == "null":
                null_count += 1
                continue
            left_index = 2 * index + 1 - 2 * null_count
            right_index = 2 * index + 2 - 2 * null_count
            if left_index >= len(node_list):
                break
            left = node_list[left_index]
            node.left = left if left != "null" else None

            if right_index >= len(node_list):
                break
            right = node_list[right_index]
            node.right = right if right != "null" else None
        return node_list[0]

lst = "[1,2,3,null,null,4,5,6,7]"
a = Codec()
print(a.serialize(a.deserialize(lst)))

