import bisect
# 前提：list有序
# bisect 方法用于探测目标值在有序list中的index
# insort 方法用于真正的去插入一个值
# 无论是探测还是插值都在右侧进行，除非指明left

lst = [1, 3, 3, 5, 8]
print(bisect.bisect(lst, 3))  # 1
print(bisect.bisect_right(lst, 3))  # 3
print(bisect.bisect_left(lst, 3))  # 1

bisect.insort(lst, 7)  # 在原list有序的前提下，插入当前数字
print(lst)  # [1, 3, 3, 5, 7, 8]
bisect.insort_left(lst, 7)  # 在原list有序的前提下，插入当前数字
print(lst)  # [1, 3, 3, 5, 7, 7, 8]
bisect.insort_right(lst, 7)  # 在原list有序的前提下，插入当前数字
print(lst)  # [1, 3, 3, 5, 7, 7, 7, 8]

