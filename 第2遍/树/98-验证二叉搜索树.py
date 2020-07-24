# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        mem, st = -float("inf"), []
        while root or st:
            while root is not None:
                st.append(root)
                root = root.left
            node = st.pop()
            if node.val <= mem:
                return False
            mem = node.val
            root = node.right
        return True

