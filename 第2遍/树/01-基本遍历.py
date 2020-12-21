# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2020/12/20 19:57

class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

root = BinTNode(1, BinTNode(2, BinTNode(4), BinTNode(5)),
                BinTNode(3, BinTNode(6), None))

def preOrder(root, lst):
    # 把以 root为根节点的树 的 先序遍历 结果放到lst中
    if root is None: return
    lst.append(root.val)
    preOrder(root.left, lst)
    preOrder(root.right,lst)

def midOrder(root, lst):
    # 把以root为根节点的数的中序遍历结果填充到lst中
    if not root: return
    midOrder(root.left, lst)
    lst.append(root.val)
    midOrder(root.right, lst)

def postOrder(root, lst):
    # 把以root为根节点的树的后序遍历 填充到 lst中
    if not root: return
    postOrder(root.left, lst)
    postOrder(root.right, lst)
    lst.append(root.val)

def preOrder2(root):
    # 根节点存入结果
    # 右节点入栈，左结点入栈
    res = list()
    cans = [root]
    while root or cans:
        root = cans.pop()
        if root:
            # 弹出本节点，说明根节点已经访问完毕
            # 先访问本节点，然后右左压栈
            res.append(root.val)
            cans.append(root.right)
            cans.append(root.left)
    return res

def midOrder2(root):
    # 中序：左 根 右
    res = []
    cans = []
    while root or cans:
        while root is not None:
            cans.append(root)
            root = root.left
        # 弹出本节点，说明本节点的左子树已经访问完毕
        node = cans.pop()
        # 先将本节点的val入栈
        res.append(node.val)
        # 再访问本节点的右节点
        root = node.right
    return res

def postOrder2(root):
    # 左-右-根
    res = []
    cans = []
    while root or cans:
        while root is not None:
            cans.append(root)
            root = root.left if root.left else root.right
        # 弹出本节点，说明左子树访问完毕了，或者左右子树都访问完毕了
        node = cans.pop()
        # 首先保存本节点的值
        res.append(node.val)
        # 然后访问 右兄弟节点
        root = cans[-1].right if cans and node is cans[-1].left else None
    return res

print(preOrder2(root))
print(midOrder2(root))
print(postOrder2(root))

