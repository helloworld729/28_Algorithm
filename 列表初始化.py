print("深拷贝初始化")
list1 = [[1, 2, 3] for i in range(3)]
print(list1)
list1[-1][-1] -= 3
print(list1)

print("浅拷贝初始化")
list2 = [[1, 2, 3]] * 3
print(list2)
list2[-1][-1] -= 3
print(list2)

# 小结：二维需谨慎，独立用range