from collections import deque

class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def count_BinTNode(t):
    if t is None:
        return 0
    else:
        total = 1 + count_BinTNode(t.left) + count_BinTNode(t.right)
    return total

total = 0
def count_BinTNode2(t):
    if t is None:  # 边界条件
        return
    else:
        global total
        total += 1
        count_BinTNode2(t.left)
        count_BinTNode2(t.right)

def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.letf) + sum_BinTNode(t.right)

def pre_order(root, lst=[]):
    if root is None:  # 边界条件
        return
    lst.append(root.data)  # 处理方法
    pre_order(root.left)   # 递归推进
    pre_order(root.right)  # 递归推进
    return lst

def mid_order(t, lst=[]):
    if t is None:
        return
    mid_order(t.left)  # 处理左子树
    lst.append(t.data)  # 处理自己
    mid_order(t.right)  # 处理右子树
    return lst

def last_order(t, lst=[]):
    if t is None:
        return
    last_order(t.left)
    last_order(t.right)
    lst.append(t.data)
    return lst

def level_order(root):
    res = []
    if root is None:
        return
    que = deque()
    que.append(root)
    while que:
        temp = que.popleft()
        res.append(temp.data)
        if temp.left is not None:
            que.append(temp.left)
        if temp.right is not None:
            que.append(temp.right)
    return res

def preorder_elements(t):
    s= []
    s.append(t)
    while len(s) > 0:
        t = s.pop()
        while t is not None:
            yield t.data
            s.append(t.right)
            t = t.left

def preorder_nonrec(root):
    # 压入右结点， 读左结点
    res, st = [], []
    st.append(root)
    while st:
        root = st.pop()
        while root is not None:
            res.append(root.data)
            st.append(root.right)
            root = root.left
    return res

def midorder_nonrec(root):
    res, st = [], []

    while st or root is not None:
        while root is not None:
            st.append(root)
            root = root.left

        node = st.pop()
        res.append(node.data)

        root = node.right
    return res

def postorder_nonrec(root):
    res, st = [], []

    while st or root is not None:
        while root is not None:
            st.append(root)
            root = root.left if root.left else root.right

        node = st.pop()
        res.append(node.data)

        if st and st[-1].left == node:
            root = st[-1].right
        else:
            root = None
    return res

root = BinTNode(0, BinTNode(1, BinTNode(3, BinTNode(7), BinTNode(8)),
                BinTNode(4, BinTNode(9), None)), BinTNode(2, BinTNode(5),
                BinTNode(6)))

print('广度优先：', end='')
print(level_order(root))
print("")
print('先序遍历：', end='')
print(pre_order(root))
print('先序遍历：', end='')
print(preorder_nonrec(root))
print('')
print('中序遍历：', end='')
print(mid_order(root))
print('中序遍历：', end='')
print(midorder_nonrec(root))
print('')
print('后序遍历：', end='')
print(last_order(root))
print('后序遍历：', end='')
print(postorder_nonrec(root))
