"""
题目：输入：nums = [-1,2,1,-4], target = 1
找到与target最接近的三数之和
"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        ll = len(nums)
        res = 0
        min_gap = float("inf")
        nums.sort()  # 排序

        for i in range(ll-3+1):
            first = nums[i]
            j = i + 1
            k = ll - 1
            temp_target = target - first
            while j < k:  # 转化为两数之和
                two_sum = nums[j] + nums[k]
                if two_sum < temp_target:
                    j += 1
                elif two_sum > temp_target:
                    k -= 1
                else:
                    return target
                if abs(first + two_sum - target) < min_gap:
                    res = first + two_sum
                    min_gap = abs(first + two_sum - target)
                    # print(first, nums[j], nums[k])
        return res


# 方法：排序 + 双指针 时间复杂度O(N2)

