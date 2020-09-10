s1 = input()
s2 = input()
def get_factor(s):
    # 从长度1开始，尝试扩大边界
    res = {s:1}
    ll = len(s)
    for l in range(1, ll):
        if ll % l != 0:
            continue
        combine = s[:l]  # 临时长度
        left, right = 0, l  # 闭区间
        flag = True
        while right <= ll:
            if s[left:right] != combine:
                flag = False
                break
            left, right = left + l, right + l
        if flag:
            res[combine] = 1
    return res

res1 = get_factor(s1)
res2 = get_factor(s2)
# print(res1, res2)
cans = list(res1.keys())
cans.sort(key=lambda x: len(x), reverse=True)

have = False
for key in cans:
    if key in res1 and key in res2:
        have = True
        print(key)
        break
if not have:
    print("")


