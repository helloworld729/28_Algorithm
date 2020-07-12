"""
负数的处理办法：
1、先取绝对值进行转换
2、结果加上符号
"""
def tobin(x):
    res = ""
    if x == 0:
        return str(0)
    while x>0:  # 一下三行是进制转换的通用部分
        res += str(x%2)
        x //= 2
    return res[::-1]  # 最后反转字符串
# print(tobin(50))
# print(bin(50))

def to_hex(x):
    res = ''
    map_dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    is_neg = x <0
    if is_neg:
        x *= -1
    while x > 0:
        temp = x % 16
        res += str(map_dic.get(temp, temp))  # key, default
        x //= 16
    if is_neg:
        return '-' + res[::-1]
    return res[::-1]
# print(to_hex(-26))


# #################################leetcode260-位运算 ##########################################
"""
260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

"""

def singleNumber(nums):
    diff = 0
    for num in nums:
        diff = diff ^ num  # 两个single num的亦或值
    diff = diff & (-diff)  # 保留最右边的1其余为变成0
    ret = [0, 0]
    for num in nums:       # 数据分组
        if (diff & num == 0):
            ret[0] = ret[0] ^ num
        else:  # 这个是diff为1的那个数所在的组
            ret[1] = ret[1] ^ num
    return ret

print(singleNumber([1,1,2,2,3,6]))