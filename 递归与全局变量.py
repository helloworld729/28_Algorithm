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