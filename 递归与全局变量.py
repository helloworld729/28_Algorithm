# 无论是普通变量还是列表，用作全局变量的话都需要global
# 不是说python全都是全局变量吗？但是在函数体内部还是不能访问
# ###################### 递归的时候，默认形参失效 ################################
lst = [1, 2, 3]
def fun(i, lst=[]):
    if i == 6:
        return
    lst.append(i)
    print(lst)
    fun(i+1)
# fun(0)
# ################################# global ########################################
# 递归不影响全局变量
# global声明的时候不可以赋值
# 外部定义变量的时候，不需要前加global声明，函数体内使用的时候必须声明，且可同时多个
flag, flag2 = True, False
def func(x):
    if x == 1:
        global flag, flag2
        flag, flag2 = False, True
        return x
    return x * func(x-1)
print(func(3))
print(flag, flag2)

