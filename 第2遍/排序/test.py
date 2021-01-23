# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 中心扩展算法：如果两侧数据一样的话就增长

def centerExpand(s, left, right):
    while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
        left, right = left-1, right + 1
    return left+1, right-1

def maxCountPart(s="abab"):
    length = len(s)
    start, end = 0, 0
    for i in range(length):
        left1, right1 = centerExpand(s, i, i+0)
        left2, right2 = centerExpand(s, i, i+1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start:end+1]


print(maxCountPart())

