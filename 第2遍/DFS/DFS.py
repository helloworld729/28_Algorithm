class Solution:
    def __init__(self):
        self.total = 0
        self.count = 0

    def findCircleNum(self, M) -> int:
        color = -1
        ll = len(M)

        def dfs(r):
            M[r][r] = color  # 自己染色
            for index, num in enumerate(M[r]):
                if num == 1:
                    self.count = 1
                    M[r][index] = color  # 朋友染色
                    M[index][r] = color  # 朋友染色
                    dfs(index)
            return

        for a in range(ll):
            dfs(a)
            if self.count == 1:
                self.count = 0
                self.total += 1

        return self.total
lst = [[1,1,0],
         [1,1,0],
         [0,0,1]]
a = Solution()
print(a.findCircleNum(lst))