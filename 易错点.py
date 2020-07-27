# ###################### 列表在函数内部不能使用 + ，但是可以直接append ###################
a = [1,2,3]
def fun():
    a = a + [4]
# fun()
print(a)

# ######################################## 写成一行的风险 ################################
a, b = 1, 3 if False else (2, 4)  # 奇葩
print(a, b)  # 1 (2, 4)，这样写相当于a无条件赋值，条件用于判断对b是复制为3还是(2,4)
(a, b) = (1, 3) if False else (2, 4)
print(a, b)  # 2 4


