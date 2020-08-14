"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
输入：nums = [3,4,3,3]
输出：4
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof

two one 本来表示某一位2进制，当前累计1的个数%3的结果
以上是对数字的二进制中 “一位” 的分析，而 int 类型的其他 31 位具有相同的运算规则，因此可将以上公式直接套用在 32 位数上。

遍历完所有数字后，各二进制位都处于状态 00 和状态 01 （取决于 “只出现一次的数字” 的各二进制位是 11 还是 00 ），
而此两状态是由 one 来记录的（此两状态下 twos 恒为 0 ），因此返回 ones 即可。

"""
class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
    def singleNumber2(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
a = Solution()
print(a.singleNumber2([1,2,3,2,3,2,3]))

