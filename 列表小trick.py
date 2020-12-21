a = [1]
print(a[2:])  # []
print(a[1:])  # []
# 列表切片不会报错
# print(a[1])
# 切片可以越界，索引不可以越界

# 列表随机采样
import random
b = [1, 2, 3]
print(random.choice(b))

