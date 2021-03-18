a = set()
a.add(1)
a.add(2)
a.remove(1)
print(a, list(a))
# {2} [2]
"""
1、hash-set：不能用index索引
2、集合无序
"""

x = {"hello", "world"}
y = {"hello", "knoght"}

print(x.difference(y))    # 差集
print(x.intersection(y))  # 交集
print(x.union(y))         # 并集

