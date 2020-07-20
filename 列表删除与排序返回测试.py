list_a = [1, 2, 3, 4, 5]
# ######################## 内嵌排序有返回 ############################
print("***内嵌排序测试***")
list_b = sorted(list_a, reverse=True)
print(list_b)  # [5, 4, 3, 2, 1]

# ######################## .sort()函数无返回 ############################
print("***.sort()函数测试***")
list_a = list_a.sort(reverse=True)
print(list_a)  # None.

# ######################## remove函数无返回 ############################
print("***remove测试***")
list_a = [1, 2, 3, 4, 5]
list_a = list_a.remove(2)
print(list_a)  # None

# ########################### pop返回pop值 ##############################
print("***pop测试***")
list_a = [1, 2, 3, 4, 5]
num = list_a.pop()
print(num, list_a)

"""
内嵌有返回，类方法无返回
结论：1、内嵌排序需要返回接收，否则不变
结论：2、类方法的sort和remove均不需要返回，pop返回弹出的值-->类方法无需返回
"""