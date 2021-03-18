from collections import deque


class TreeNode(object):
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []

        res = []
        cans = deque()
        cans.append(root)

        while cans:
            root = cans.popleft()
            if root:
                res.append(root.val)
                cans.append(root.left)
                cans.append(root.right)
            else:
                res.append("None")
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        # data = data[1:-1].split(",")  # 题目在这里传过来的不是str
        # 因为节点中可能出现0，所以判0与判None可能混淆，所以以后尽量用精确模式，不要省略
        data = list(map(lambda x: int(x) if x != "None" else None, data))

        data = list(map(lambda x: TreeNode(x) if x is not None else x, data))

        None_counts = 0

        for i in range(len(data)):
            if data[i] is not None:
                data[i].left = data[2 * i + 1 - 2 * None_counts]
                data[i].right = data[2 * i + 2 - 2 * None_counts]
            else:
                None_counts += 1
        return data[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# 关键点在于节点的索引关系：2*i+1, 2*i+2。如果前面出现了None，那么索引退化2*None_counts
# 个，即None节点不会再产生空节点，所以在求自己左右节点的时候，要缩短相应的距离。
# 还有就是空节点就是None，而不是一个value为None的树节点。

