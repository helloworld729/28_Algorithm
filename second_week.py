import re
# 第一题 正则替换
def replaceSpace(s):  #
    """替换空格
    请实现一个函数，将一个字符串中的每个空格替换成“%20”。
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
    """
    return re.sub(" ", "%20", s)

# 第二题 正则匹配
def match(s, pattren):
    """
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
    """
    ans = re.findall(pattren, s)
    for a in ans:
        if len(a)==len(s):
            return True
    return False

# 第三题 表示数值的字符串
def isNum(s):
    """
    https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
    """
    ans = re.match(r"^[-+]?\d*(?:\.\d*)?(?:[eE][+\-]?\d+)?$", s)
    if ans:
        return True
    return False

# 第四题 第一个不重复的字符
def firstAppear(s):
    """
    请实现一个函数用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

    思路： 对撞指针
    """
    cache = []
    rep = []  # 空间换时间
    l, end = 0, len(s) - 1
    while l <= end:
        r = end
        if s[l] not in rep:
            while r > l:
                if s[r] != s[l]:
                    r -= 1
                else:
                    break
            if r == l:
                cache.append(s[l])
            else:
                rep.append(s[l])
        l += 1

    if cache:
        return cache[0]
    elif s[-1] not in rep:
        return s[-1]
    else:
        return "#"

# print(firstAppear("aabbc"))

# 第五题 旋转字符串
def LeftRotateString(s, n):
    # write code here
    try:
        n = n % len(s)
    except:
        return s
    return s[n:] + s[:n]
# print(LeftRotateString("asdf", 6))

def RightRotateString(s, n):
    try:
        n = n % len(s)
    except:
        return s
    return s[-n:] + s[n:]
# print(RightRotateString("", 1))

# 第六题 字符串排列
def Permutation(ss):
    """https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7"""
    ans = []
    # write code here
    if len(ss) == 1:                                # 边界条件
        ans.append(ss)
    else:
        for i in range(len(ss)):                    # 遍历可能
            self = ss[i]
            other = Permutation(ss[:i] + ss[i+1:])  # 递归推进
            for ele in other:
                ans.append(self + ele)              # 处理办法
    return ans                                      # 递归返回

print(Permutation("abc"))
