def q_sort0(lst, l, r):
    """
    快速排序
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :return:
    """
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

    q_sort0(lst, l, i-1)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面
    q_sort0(lst, i+1, r)  # 递归推进，右侧快排，

    return lst


def q_sort(lst, l, r, k):
    """
    快速排序
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :param k: 返回第K大的元素，如果pivot位置在k右边，那么右边的部分不用继续排序
    :return:
    """
    if k <= 0:
        return None
    # l, r = 0, len(lst) - 1
    if l >= r:  # 边界条件，只有一个元素
        return lst[l]

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:  # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止, 第一个条件保证第一个数最小时数组不会越界
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

    if i == k - 1:
        return lst[i]
    elif i < k - 1:
        return q_sort(lst, i+1, r, k)  # 递归推进，右侧快排，由于i和k都是全局的所以k不变
    elif i > k - 1:
        return q_sort(lst, l, i-1, k)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面


a = [3,4,6,5]
for i in range(1, len(a)+1):
    result = q_sort(a,l=0,r=len(a)-1,k=i)
    print(result)

"""
反向遍历的两种方法：
1、在向下递归的过程中，控制区间, 变量始终是一个变量
2、在向下递归的过程中，列表切片, 但是这样相当于创建了一个新的变量
应该采用第一种方法较好

快拍思路：pivot-partition
易错点：递归的时候以pivot为分界线，而不是middle，也没有middle
"""