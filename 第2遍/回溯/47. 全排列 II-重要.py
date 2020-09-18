class Solution:
    def permuteUnique(self, nums):
        res = []
        def back(have, cans):
            # dfs
            ll = len(cans)
            if not ll:
                res.append(list(have))
                return

            for i in range(ll):
                if cans[i] in cans[:i]:
                    continue
                have.append(cans[i])
                back(have, cans[:i] + cans[i+1:])
                have.pop()
        back([], nums)
        return res

    def permuteUnique2(self, nums):
        def back(have, cans):
            # 回溯
            ll = len(cans)
            if not ll: return [[]]

            temp = []
            for i in range(ll):
                if cans[i] in cans[:i]:
                    continue
                have.append(cans[i])
                for data in back(have, cans[:i] + cans[i+1:]):
                    temp.append([cans[i]] + data)
                have.pop()
            return temp

        res = back([], nums)
        return res

"""
分析：
第一种方法实际上是dfs
第二种方法是回溯，有一个非常值得注意的问题：
当我们的cans是字符串的时候，边界return为[""]
当我们的cans是list  的时候，边界return为[[]]

两种情况下，都不能绝对不要写成[]，因为这样不会进入到29行的for循环中，无法
添加最底层的字符，结果每一层返回的都是空列表
"""








