nums = [-1, 1, -1, 1]
def max_same(nums):
    prefix = {0: -1}  # sum:index
    temp = 0
    max_len = 0
    for i in range(len(nums)):
        temp += nums[i]
        if temp in prefix:
            max_len = max(i-prefix[temp], prefix[temp])
        else:
            prefix[temp] = i
    return max_len

# 1,-1 ########### -1 如果#位置的1和-1一样多的话，那么
# 如果我们求前缀和的话，最后的时候 会发现 前缀和为0已经出现了。
# 那么这个时候可以求出 # 的长度 也就是和为0的子串的长度

# 求出“11110001”中0和1个数相等的子串

def max_sames(s):
    prefix = {0:-1}
    temp = 0
    l, r = 0, 0
    for i in range(len(s)):
        temp += 1 if s[i] == "1" else -1
        if temp in prefix and i - prefix[temp] > r - l:
            l, r = prefix[temp] + 1, i  # 左边界要叫1
        else:
            prefix[temp] = i
    return s[l: 1+r] if l != r else None

s = "111101011"
print(max_sames(s))

# 用哈希表与前缀和

