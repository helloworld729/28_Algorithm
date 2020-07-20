"""
小写>大写>奇数>偶数
记得顺序倒过来写，因为满足为1，正常序放在后面；X放在最后相当于"个位"影响因子最小
"""
s = "Sorting3214"
s = list(s)
print("原始S：", s)
s = sorted(s, key=lambda x: (x.isdigit() and int(x)%2==0, x.isdigit() and int(x)%2==1, x.isupper(), x.islower(), x))
print("排序S：", s)
# ##############################################################################
# 首先按照值value排序，value一致按照key排序
a = {"a":1, "bc":2, "c":3, "ab": 2}
print(a)
f = lambda x: (x[1], x[0])  # 多级排序
print(sorted(a.items(), key=f))

