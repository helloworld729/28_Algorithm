class test():
    def __init__(self):
        self.data = 0
        self.lst = [1,2,3,4,5]

    def __iter__(self):
        for i in range(5):
            self.data += 1
            yield self.data

    def __next__(self):
        self.data += 1
        if self.data < 10:
            return self.data
        else:
            raise StopIteration



t = test()  # test
# for i in range(5):
#     print(t.__next__())
# for i in t:
#     print(i)
lst = [1,2,3]
lst = (d for d in lst)
for i in range(5):
    print(next(lst))