class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def cal_weight(x):
            if x == 1:
                return 0
            if x%2 == 0:
                return 1 + cal_weight(x // 2)
            return 1 + cal_weight(3 * x + 1)
        weight_dict = {i:0 for i in range(lo, hi+1)}
        for i in range(lo, hi+1):
            weight_dict[i] = cal_weight(i)
        print(weight_dict)
        f = lambda x: str(x[1]) + str(x[0])
        res = sorted(weight_dict.items(), key=lambda x:(x[1], x[0]))
        print(res)
        return res[k-1][0]
a = Solution()
print(a.getKth(12, 15, 2))