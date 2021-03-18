# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2020/12/18 14:55

# from tqdm import tqdm
# a = ["a", "b", "c"] * 1000000
# for d in tqdm(a, leave=True):
#     0
#

# ################### 多级生成器测试 ####################
# 每4个构成一个编组
def first():
    temp = list()
    for i in range(1, 12+1):
        temp.append(i)
        if i and i % 4 == 0:
            yield temp
            temp = list()

def second():
    temp = list()
    for data in first():
        # 每2个构成一个编组
        temp.extend(data)
        if len(temp) >= 2:
            temp2 = list()
            for j in range(len(temp)):
                temp2.extend([temp[j]])
                if len(temp2) == 2:
                    yield temp2
                    temp2 = list()

        temp = list()

# for data in second():
#     print(data)

# [1, 2]
# [3, 4]
# [5, 6]
# [7, 8]
# [9, 10]
# [11, 12]


# ################### 生成器next测试 ####################
def myGenerator():
    temp = list()
    for i in range(1, 1+100):
        temp.append(i)
        if len(temp) == 4:
            yield temp
            temp = list()
gene = myGenerator()

def fun1(ge):
    a = next(ge)
    print(a)

def fun2(ge):
    b = next(ge)
    print(b)

fun1(gene)
fun2(gene)
# 说明generator有一个全局的指针，无论在哪里使用了next

