from copy import copy
class Max_sum():
    def __init__(self, lst):
        self.max_sum = -float("inf")
        self.res = []
        self.lst = lst
        self.count = 4  # N个数减1
        self.dis = 2  # 距离
    def dfs(self, index, count, choose):
        if count == self.count:  # 控制长度
            choose.append(index)
            result = list(map(lambda x: self.lst[x], choose))
            if sum(result) > self.max_sum:
                # print(sum(result))  # 综合
                self.max_sum = sum(result)
                self.res = result
            return

        for next_pos in [index+i for i in range(1, self.dis+1)]:  # 控制距离
            if next_pos <= len(self.lst)-1:
                choose_back = copy(choose)
                choose_back.append(index)
                self.dfs(next_pos, count+1, choose_back)

                
lst = [10, 1, 5, 3, 8, 5, 6, 200, 7, 2, 9, 100]
result = Max_sum(lst)
for index in range(len(lst)):
    choose = []
    result.dfs(index, 0, choose)  # 目标index， 当前数目， 当前和
print(result.max_sum, result.res)
