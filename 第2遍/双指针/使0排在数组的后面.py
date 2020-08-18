# 仍然是一次partition操作，但是具有稳定性
# 也可以用这种方法处理奇偶的partition操作

def not_zero(lst):
    l = r = 0
    length = len(lst)-1
    while r < length:
        while l < length and lst[l] != 0:  # 左边界指向0
            l += 1
        while r < length and lst[r] == 0:  # 右边界指向!0
            r += 1
        lst[l] = lst[r]
        lst[r] = 0

lst = [0,0,1,2,3,0,0,0,0,0,5,9,8,0,0,0]
not_zero(lst)
print(lst)