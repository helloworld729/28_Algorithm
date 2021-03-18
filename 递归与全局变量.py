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
# 6
# False True

# ############################ global yu  nonlocal ################################

# 第一，两者的功能不同。global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，
# 而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，
# nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
#
# 第二，两者使用的范围不同。global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，
# 即使之前未定义该变量，global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，
# 并且外层函数中定义了相应的局部变量，否则会发生错误（见第一）。
# https://blog.csdn.net/xcyansun/article/details/79672634

