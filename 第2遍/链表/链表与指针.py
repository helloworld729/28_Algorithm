class linknode():
    def __init__(self, val):
        self.val = val
        self.next = None
def print_link(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

a = linknode(1)
b = linknode(2)
c = linknode(3)

# ####################### 顺序连接 #############################
a.next = b
b.next = c

head = a
while head:
    print(head.val, end=" ")
    head = head.next
print()

# ####################### 逆序连接 #############################
b.next = c
a.next = b
head = a
while head:
    print(head.val, end=" ")
    head = head.next
print()

# ####################### 伪链表头 #############################
p = head = linknode(0)
for i in range(1, 6):
    node = linknode(i)
    head.next = node
    head = head.next
p = p.next  # 变成真头
while p:
    print(p.val, end=" ")
    p = p.next
print()
# ####################### 新增节点 #############################
p = head = linknode(0)
for i in range(1, 6):
    node = linknode(i)
    head.next = node
    head = head.next
p = p.next  # 变成真头
print("初始化为：")
print_link(p)
print("add 3.5 behind 3")
q = p  # 分身
while q:
    if q.val == 3:
        node = linknode(3.5)
        node.next = q.next
        q.next = node
        break
    q = q.next
print_link(p)

"""


"""