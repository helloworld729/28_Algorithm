**题目1-平衡二叉树**<br>
给定一个二叉树，判断它是否是高度平衡的二叉树。<br>
本题中，一棵高度平衡二叉树定义为：<br>
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。<br>

**示例 1**:<br>

给定二叉树 [3,9,20,null,null,15,7]<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp; \\<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;20<br>
&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;\\<br>
15&nbsp;&nbsp;&nbsp;&nbsp;7<br>
返回 true 。<br>
来源 leetcode 110


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        @staticmethod
        def tree_len(node):
            if node.left is None and node.right is None:
                return 0
            t_len = 1 + max(tree_len(node.left), tree_len(node.right))
            return t_len
        
        if root is None:
            return True
        left_height = self.tree_len(root.left)
        right_height = self.tree_len(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
```


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree_len(self, node):
            if node is None:
                return 0
            t_len = 1 + max(self.tree_len(node.left), self.tree_len(node.right))
            return t_len

    def isBalanced(self, root):
        if root is None:
            return True
        left_height = self.tree_len(root.left)
        right_height = self.tree_len(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)   
```

实践表明：尽量不要用静态函数，因为速度慢<br>
这题应该可以用动规加速，后面可以试一下。


```python

```

**题目2-层次遍历**<br>
找树左下角的值，给定一个二叉树，在树的最后一行找到最左边的值.<br>

**示例:**<br>
输入:<br>

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:<br>
7 <br>

注意: 您可以假设树（即给定的根节点）不为 NULL。<br>
来源：leetcode513<br>

思路：<br>
从由向左进行层次遍历<br>


```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        que = [root]
        while que:
            node = que.pop(0)
            if node.right is not None:
                que.append(node.right)
            if node.left is not None:
                que.append(node.left)
        return node.val
```


```python

```

**题目-3. 二叉树的前序遍历**<br>
给定一个二叉树，返回它的 前序 遍历。<br>

**示例:**<br>
输入: [1,null,2,3]  <br>
&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;\ <br>
&nbsp;&nbsp;&nbsp;&nbsp;2<br>
&nbsp;&nbsp;&nbsp;/<br>
&nbsp;&nbsp;3<br>

**输出:** [1,2,3]<br>
**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？<br>
来源：144


```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self,):
        self.res = []
    def preorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res
```


```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self,):
        self.res = []
        self.st = []
    def preorderTraversal(self, root: TreeNode):
        """先序遍历"""
        if not root:
            return []
        self.st.append(root)
        while self.st:
            node = self.st.pop()
            
            while node is not None:
                self.res.appned(node.val)
                self.st.append(node.right)
                node = node.left     
        
        return self.res
```


```python

```

**题目4**<br>
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。<br>

**说明**：<br>
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。<br>

示例:<br>
输入: root = [5,3,6,2,4,null,null,1], k = 3<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp; \ <br>
&nbsp;&nbsp;&nbsp;&nbsp; 3 &nbsp;&nbsp;&nbsp;6<br>
&nbsp;&nbsp;&nbsp;&nbsp;/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\ <br>
&nbsp;&nbsp; 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4<br>
&nbsp;&nbsp;/<br>
 1<br>
输出: 3<br>
进阶：<br>
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？<br>

来源：力扣230（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.index = 0
        self.st = []

        while self.st or root is not None:
            while root is not None:
                self.st.append(root)
                root = root.left
            node = self.st.pop()
            self.index += 1
            if self.index == k:
                return node.val

            if node.right is not None:
                root = node.right
            else:
                root = None
```
