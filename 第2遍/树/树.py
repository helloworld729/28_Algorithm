
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


