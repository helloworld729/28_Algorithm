# leetcode100-相同的树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:
        # 边界条件
        if p is None and q is None:
            return True
        if type(p) != type(q):
            return False

        # 递归推进
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False

# 判断是否镜像对称
class Solution:
    def isSymmetric(self, root) -> bool:
        def symmetry(p, q):
            # 边界条件
            if type(p) != type(q):
                return False
            elif p is None and q is None:
                return True

            if p.val == q.val and symmetry(p.left, q.right) and symmetry(p.right, q.left):
                return True
            return False

        if root is None:
            return True
        return symmetry(root.left, root.right)

# 树的层次遍历-102题目
# 要把结果分层-技巧就是：用根节点初始化队列后，每一层要访问的节点数目就是当时队列的长度
from collections import deque
class Solution:
    def levelOrder(self, root):
        levels = []  # 层次遍历结果
        if not root:
            return levels

        level = 0  # 层数
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return levels

# 二叉排序树的生成
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)

                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n) if n else []


