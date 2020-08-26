import heapq
lst = [7, 2, 5, 7, 3, 4]
# ##################### 第一种方式 ###################################
# h = []  # 堆容器
# for i in lst:
#     heapq.heappush(h, i)  # 入堆
# print(heapq.heappop(h))   # 出堆
# print(heapq.nsmallest(2, h))  # 最大的前n个数（不推荐）
# print(heapq.nlargest(2, h))   # 最小的前n个数

# ##################### 第二种方式 ###################################
heapq.heapify(lst)
# lst.heappush(6)
for i in range(len(lst)):
    print(heapq.heappop(lst))
# print(heapq.nsmallest(2, lst))
# print(heapq.nlargest(2, lst))
# ######################### 小结 ######################################
# heapify 将lst转化为堆，如果lst已经是正常堆序列，那么可以没有这一步
# 假如lst不是堆序，又没有heapify那么结果是错的。
# 转化为堆的方法：1、逐个heapq.heappush();2、直接heapify()
# trick：默认小顶堆-->大顶堆 ## 反入-出反

