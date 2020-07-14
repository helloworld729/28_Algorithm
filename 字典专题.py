# ############################ 字典排序 #######################################
def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按值(value)排序:")
    res = sorted(key_value.items(), key=lambda kv: kv[1])  # 返回键值对元组列表
    print(res)

# dictionairy()

# ############################ 字典 #######################################