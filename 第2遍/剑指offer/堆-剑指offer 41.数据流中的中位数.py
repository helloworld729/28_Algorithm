import heapq

class MedianFinder:
    def __init__(self):
        self.a = []  # 小顶堆，存储较大的数据
        self.b = []  # 绝对值大顶堆，存储较小的数据
        self.m = self.n = 0  # 数据长度

    def addNum(self, num: int) -> None:
        # 需要向a插入数据，从b向a迂回
        if self.m == self.n:
            heapq.heappush(self.b, -num)
            heapq.heappush(self.a, -heapq.heappop(self.b))
            self.m += 1
        else:
            heapq.heappush(self.a, num)
            heapq.heappush(self.b, -heapq.heappop(self.a))
            self.n += 1

    def findMedian(self) -> float:
        if self.m == 0: return None
        return self.a[0] if (self.m + self.n) & 1 else 0.5 * (self.a[0] - self.b[0])  # 取负号


# 思路：建立两个堆a, b分别用来存 教大的数和较小的数据
# 并且用m, n表示对堆的长度，规定m>=n,即m ！= n时，存到b
# m==n时，存到a，那么中位数由两个堆顶决定。