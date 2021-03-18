
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
# 输入：nums = [3,4,3,3]
# 输出：4
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof

# 统计各个二进制位 数字1 出现的次数
# 定义two one 表示某一位 1的个数除以3取余后的结果
# two one 含义：
# 0   0   该位 取余后 有0个1
# 0   1   该位 取余后 有1个1
# 1   0   该位 取余后 有2个1

# x^0 = x; x^1=~x

class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

a = Solution()
print(a.singleNumber([5,2,3,2,3,2,3]))

