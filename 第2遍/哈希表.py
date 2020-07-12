# 题目1 同度最短子串-697
class Solution:
    def findShortestSubArray(self, nums) -> int:
        count, span = {}, {}  # 次数统计，某数字在nums的区间统计
        target_num = []  # 度最高的数字
        degree = 0  # 最大的度
        for index, num in enumerate(nums):
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > degree:
                degree = count[num]
                target_num = [num]
            elif count[num] == degree:
                target_num.append(num)

            if num not in span:
                span[num] = [index, index]
            else:
                span[num][-1] = index

        res = span[target_num[0]][1] - span[target_num[0]][0] + 1  # 第一个候选区间范围
        for num in target_num[1:]:
            res = min(res, span[num][1] - span[num][0] + 1)
        return res
a = Solution()
print(a.findShortestSubArray([1,2,3,2,1,2,1,2,5]))