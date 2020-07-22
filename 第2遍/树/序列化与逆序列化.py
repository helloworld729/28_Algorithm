# ################ 剑指 Offer 37. 序列化二叉树 ##############################
# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/submissions/
# 小结：对序列化列表分割首选re.sub，因为可以针对,和[]分割，注意首尾为空
# index规则，null_mem。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import re
from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return "[]"
        res, que = [], deque()
        que.append(root)
        while len(que) > 0:
            root = que.popleft()
            if root == "null":
                res.append("null")
            else:
                res.append(str(root.val))
                left = root.left if root.left else "null"
                que.append(left)
                right = root.right if root.right else "null"
                que.append(right)

        while res[-1] == "null":
            res.pop()

        res = "[" + ",".join(res) + "]"
        # print(res)
        return res

    def deserialize(self, data):  # str到root
        if data == "[]":
            return []
        null_count = 0
        data = re.split(r",|\[|\]", data)
        data = data[1:-1]

        def to_node(num): return "null" if num == "null" else TreeNode(int(num))
        node_list = list(map(to_node, data))

        for index, node in enumerate(node_list):
            # print(index)
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

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))