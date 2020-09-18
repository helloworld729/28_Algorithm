from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def subStructure(a, b):
            if not b: return True
            if not a: return False
            if a.val != b.val: return False
            return subStructure(a.left, b.left) and subStructure(a.right, b.right)

        if not B: return False

        que = deque()
        que.append(A)

        while que:
            root = que.popleft()
            if root.val == B.val:
                flag = subStructure(root, B)
                if flag: return True
            if root.left:  que.append(root.left)
            if root.right:  que.append(root.right)
        return False

"""
复杂度分析：
时间复杂度 O(MN)：其中 M,N 分别为树A和树B的节点数量；
先序遍历树A占用 O(M)，每次调用 recur(A, B) 判断占用O(N)。

空间复杂度 O(M) ： 当树 AA 和树 BB 都退化为链表时，递归调用深度最大。
当 M≤N 时，遍历树A 与递归判断的总递归深度为M ；当 M>N时，
!!!最差情况为遍历至树A 叶子节点，此时总递归深度为M。

"""