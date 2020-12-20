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
    if root is None: return []
    result = []
    cans = [root]
    while cans:
        root = cans.pop()
        if root:
            result.append(root.val)
            cans.append(root.right)
            cans.append(root.left)
    return result

def midOrder2(root):
    res = []
    cans = []
    while root or cans:
        while root:
            cans.append(root)
            root = root.left
        node = cans.pop()
        # 能弹出到本节点 说明左子树已经访问完毕
        # 先访问本 根节点
        res.append(node.val)
        # 然后切换到右子树
        root = node.right
    return res

def postOrder2(root):
    res = []
    cans = []
    while cans or root:
        while root:
            cans.append(root)
            root = root.left if root.left else root.right
        # 访问到本节点，说明左右子树已经访问完毕
        node = cans.pop()
        res.append(node.val)
        # 如果有右兄弟，就切换到右兄弟，否则为弹出 父节点左准备(另root为None)
        root = cans[-1].right if cans and node == cans[-1].left else None
    return res


pre, mid, post = list(), list(), list()
preOrder(root, pre)
midOrder(root, mid)
postOrder(root, post)

print(pre)
print(preOrder2(root))
print(mid)
print(midOrder2(root))
print(post)
print(postOrder2(root))

