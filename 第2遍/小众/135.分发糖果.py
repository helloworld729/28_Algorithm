class Solution:
    def candy(self, ratings) -> int:
        ll = len(ratings)
        if ll == 1: return 1

        candy_left = [1] * ll
        candy_right = [1] * ll

        for i in range(1, ll):
            if ratings[i] > ratings[i - 1]:
                candy_left[i] = candy_left[i - 1] + 1

        for i in range(ll-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_right[i] = candy_right[i + 1] + 1

        for i in range(ll):
            candy_left[i] = max(candy_left[i], candy_right[i])

        return sum(candy_left)

lst = [1, 3,5,4,2]
a = Solution()
print(a.candy(lst))

"""
输入一个数组代表每个小朋友的分数，谈过按照以下规则分配：
1.每个孩子至少分配到 1 个糖果。
2.相邻的孩子中，评分高的孩子必须获得更多的糖果。

思路1：
先从左到右按照规则2遍历一遍，再从右到左按照规则2遍历一遍
按照每一个pos的max定出left和right的最后结果
求和，返回
https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/

"""

