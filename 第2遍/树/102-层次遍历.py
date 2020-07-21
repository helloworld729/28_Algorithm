# 树的层次遍历-102题目
# 要把结果分层-技巧就是：用根节点初始化队列后，每一层要访问的节点数目就是当时队列的长度
from collections import deque
class Solution:
    def levelOrder(root):
        que = deque()
        que.append(root)
        res = []
        if root is None:
            return []

        while que:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(level)
        return res
