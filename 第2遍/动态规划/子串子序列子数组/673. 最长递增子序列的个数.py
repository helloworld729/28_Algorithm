# 最长递增子序列的个数
# 给定一个未排序的整数数组，找到最长递增子序列的 个数。例如输入 [1,3,5,4,7]那么输出为 2，
# 因为 [1, 3, 4, 7] 和[1, 3, 5, 7]，但是 [2,2,2]要返回3。
# 难点在于：要分为是否为第一次遇到全局最值，还是第二次遇到全局最值，从而决定是set 还是 add

from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]):
        length = len(nums)
        # 到该位置最长序列长度
        lenList = [1] * length
        # 到该位置有几个序列可以达到最长
        countList = [1] * length

        # 全局最长序列的长度
        max_len = 1
        # 全局最长序列的个数
        max_len_count = 0

        for i in range(length):
            for j in range(i):
                # 第一次遇到有效增长点
                if nums[i] > nums[j]   and lenList[i] < lenList[j] + 1:
                    lenList[i] = lenList[j] + 1
                    countList[i] = countList[j]
                # 再次遇到同一增长点
                elif nums[i] > nums[j] and lenList[i] == lenList[j] + 1:
                    countList[i] += countList[j]
            # 第一次到达全局最长
            if lenList[i] > max_len:
                max_len = lenList[i]
                max_len_count = countList[i]
            # 再一次到达全局最长
            elif lenList[i] == max_len:
                max_len_count += countList[i]

        return max_len_count


print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7]))

# 1, 2, 4, 3, 5, 4, 7
# 1  2  3  3  4  4  5
# 1  1  1  1  2  1  3

# 1 2 4 5 7
# 1 2 3 5 7
# 1 2 3 4 7

