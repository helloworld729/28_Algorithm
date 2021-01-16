# ############################ 字典排序 #######################################
def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按值(value)排序:")
    res = sorted(key_value.items(), key=lambda kv: kv[1])  # 返回键值对元组列表
    print(res)

# dictionairy()

# ############################ 字典 工厂模式 #######################################
# 默认模式创建的，例如默认采用int类型，可以直接dict_a[0] + 1
from collections import defaultdict
dict_a = defaultdict(list)
for i in range(3):
    dict_a[i].append("hello")
print(dict_a)

# ############################ 字典 update #######################################
dict_a.update({2: ["world"]})  # {0: ['hello'], 1: ['hello'], 2: ['hello']}
print(dict_a)  # {0: ['hello'], 1: ['hello'], 2: ['world']}

# ############################ 字典 拷贝 #########################################
# 浅拷贝的时候假如value为简单对象，则独立赋值，复杂对象(list)还是同一块内存
# 深拷贝完全独立

# ############################ value=None ########################################
# value为None，确实为None
# path = {i: None for i in range(1, 5+1)}
# print(path)
# print(path[1] is None)
# {1: None, 2: None, 3: None, 4: None, 5: None}
# True
# ############################ setdefault ########################################
a = dict()
a.setdefault("hello", "world")
a.setdefault("hello", "world2")
print(a)
# {'hello': 'world'}
# setdefault(k, v)就是说，有k的话把他取出来，没有的话设置为v

