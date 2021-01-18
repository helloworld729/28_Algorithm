def qSort(lst, l, r):
    if l >= r:  # 边界条件，只有一个元素
        return

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot 存储

    while i < j:    # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置

    qSort(lst, l, i-1)  # 递归推进，左侧快排，
    qSort(lst, i+1, r)  # 递归推进，右侧快排，

    return lst

# 值得注意的地方：推进的过程中要跳过i，否则会陷入死循环之中
# 例如右侧推进的时候如果是从i到r，那么由于i已经是最小，而每次又选择首元素作为pivot那么
# 每一次partition都不会变。

def numK(nums, l, r, k):
    # 在区间[l, r]之间找到第k大的数字
    if l > r: return
    if l == r and len(nums) - l == k: return nums[l]

    i, j = l, r
    pivot = nums[i]
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        if i < j and nums[j] < pivot:
            nums[i] = nums[j]
            i += 1
        while i < j and nums[i] <= pivot:
            i += 1
        if i < j and nums[i] > pivot:
            nums[j] = nums[i]
            j -= 1
    nums[i] = pivot  # 还是需要的

    pos = len(nums) - i  # 位置表示第几大
    if pos == k: return nums[i]
    elif pos < k: return numK(nums, l, i-1, k)
    else: return numK(nums, i+1, r, k)

"""
反向遍历的两种方法：
1、在向下递归的过程中，控制区间, 变量始终是一个变量
2、在向下递归的过程中，列表切片, 但是这样相当于创建了一个新的变量
应该采用第一种方法较好

快拍思路：pivot-partition
易错点：递归的时候以pivot为分界线，而不是middle，也没有middle
"""