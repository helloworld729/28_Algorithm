# leetcode167-对撞指针（两数之和）
def twoSum(nums, target):
    """

    :param nums: 列表
    :param target: 目标值
    :return:
    """
    l, r = 0, len(nums)-1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return None

# print(twoSum([2,7,11,12], 23))
# ###################################################################################
# 第二题 leetcode215-快排
def q_sort(nums, l, r):
    if l >= r:  # 边界条件
        return
    i, j = l, r
    pivot = nums[i]  # 基准
    while i < j:     # 处理方法
        while i < j and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        if i < j:
            nums[j] = nums[i]
    nums[i] = pivot

    q_sort(nums, l, i - 1)  # 递归推进
    q_sort(nums, i + 1, r)

# nums = [4, 3, 5, 6,1,2,3,6,5,9,8,56]
# q_sort(nums, 0, len(nums) - 1)
# print(nums)
# ###################################################################################
# 第二题扩展-仅第K大的数
def q_sort2(nums, l, r, k):
    # if k <= 0:
    #     return None
    # if k > len(nums):
    #     k = len(nums)

    if l >= r:  # 边界条件
        return nums[r]
    i, j = l, r
    pivot = nums[i]  # 基准
    while i < j:     # 处理方法
        while i < j and nums[j] <= pivot:
            j -= 1
        if i < j:
            nums[i] = nums[j]
        while i < j and nums[i] >= pivot:
            i += 1
        if i < j:
            nums[j] = nums[i]
    nums[i] = pivot
    print(i, nums)


    if i == k-1:
        return nums[i]
    elif i < k-1:
        return q_sort2(nums, i+1, r, k)  # 由于i具有全局性，所以k不变
    else:
        return q_sort2(nums, l, i-1, k)


# nums = [3,2,3,1,2,4,5,5,6]
# # # q_sort(nums, 0, len(nums)-1)  # [1, 2, 2, 3, 3, 4, 5, 5, 6]
# # # print(nums)
# print(q_sort2(nums, 0, len(nums) - 1, 8))
# ###################################################################################
# 第二题扩展-堆排序.时间比快排少一个数量级
class Solution:
    class PrioQue():
        def __init__(self, elist):
            """设置小 优先级高"""
            self._elements = list(elist)
            self._len = len(self._elements)
            if elist:
                self.buildheap()

        def buildheap(self):
            end = self._len
            # 节点end的父节点为end//2-1
            for i in range(end // 2 - 1, -1, -1):  # 中间的-1取不到，是左闭右开区间
                self.sift_down(self._elements[i], i, end)

        def is_empty(self):
            return self._len == 0

        def dequeue(self):
            # if self.is_empty():
            #     raise PrioQueueError
            first = self._elements[0]
            last = self._elements.pop()
            self._len -= 1
            if self._len > 0:
                self.sift_down(last, 0, self._len)
            return first

        def sift_down(self, data, begin, end):
            """begin可以视作根节点，从该处三角下筛"""
            """下筛的时候就不考虑原根节点了"""
            base_pos, target = begin, 2 * begin + 1
            while target < end:  # 确定最小的→交换
                if target + 1 < end and self._elements[target] < self._elements[1 + target]:  # 第一个条件防止没有右子树
                    target += 1
                if data > self._elements[target]:
                    break  # 是三值中最小的，位置对
                else:
                    self._elements[base_pos] = self._elements[target]
                base_pos, target = target, target * 2 + 1
            self._elements[base_pos] = data
            return

    def findKthLargest(self, nums, k: int) -> int:
        pq = self.PrioQue(nums)  # [2, 4, 5, 6, 7, 9]
        for _ in range(k):
            res = pq.dequeue()
        return res
a = Solution()
print(a.findKthLargest([2, 4, 5, 6, 7, 9], 2))


# ###################################################################################
# 第三题-荷兰国旗
def sortColors(nums) -> None:  # 44ms
    """
    Do not return anything, modify nums in-place instead.
    """
    cnts = [0] * 3
    for num in nums:
        cnts[num] += 1
    index = 0
    for data, ms in enumerate(cnts):
        for i in range(ms):
            nums[index] = data
            index += 1
# nums=[1,0,1,2,0,2]
# sortColors(nums)
# print(nums)
# ###################################################################################
# 第三题-三项切分快排
def sortColors2(nums) -> None:  # 40ms
    head, tail, now = 0, len(nums)-1, 0

    while now <= tail:  # now=
        if nums[now] == 2:
            nums[now], nums[tail] = nums[tail], nums[now]
            tail -= 1
        elif nums[now] == 0:
            nums[now], nums[head] = nums[head], nums[now]
            head += 1
            now += 1
        else:
            now += 1

# nums=[1,0,1,2,0,2]
# sortColors2(nums)
# print(nums)
# ###################################################################################
# 第四题-贪心455
def findContentChildren(g, s) -> int:
    g.sort(), s.sort()

    g_index, s_index = 0, 0
    while g_index < len(g) and s_index < len(s):
        if g[g_index] <= s[s_index]:
            g_index += 1
        s_index += 1
    return g_index

# print(findContentChildren(g=[1,2,3], s=[1,1,2,3]))
# ###################################################################################