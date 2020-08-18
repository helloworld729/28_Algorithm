"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
方法1：递归+返回
方法2：单向递归
方法2：迭代
方法3：队列
"""
class Solution:
    def maxDepth(self, root) -> int:
        """递归返回60ms"""
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth2(self, root) -> int:
        """单向递归50ms"""
        max_deepth = 0
        def maxdep(root, level):
            nonlocal max_deepth
            max_deepth = max(max_deepth, level)
            if root.left:
                maxdep(root.left, level+1)
            if root.right:
                maxdep(root.right, level+1)
        if not root: return 0
        maxdep(root, 1)
        return max_deepth

    def maxDepth3(self, root) -> int:
        """队列45ms"""
        from collections import deque
        if not root: return 0
        que = deque()
        que.append((root, 1))
        max_dep = 0
        while que:
            root, level = que.popleft()
            max_dep = max(max_dep, level)
            if root.left:
                que.append((root.left, level+1))
            if root.right:
                que.append((root.right, level+1))
        return max_dep

# 代码增加 != 耗时增加


