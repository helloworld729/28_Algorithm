class Solution:  # 插入排序
    def findKthLargest(self, nums, k: int) -> int:
        temp = []
        for ele in nums:
            pos = len(temp)  # 牛B
            for i in range(len(temp)):
                if ele > temp[i]:
                    pos = i
                    break
            temp.insert(pos, ele)
        return temp[k-1]

# a = Solution()
# print(a.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))



class Solution2:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

# a = Solution2()
# print(a.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

############################# 第2题 #################################
class Solution22:
    """很烂的算法"""
    def topKFrequent(self, nums, k: int):
        info = {}
        for ele in nums:
            if ele not in info.keys():
                info[ele] = 1
            else:
                info[ele] += 1

        fre = list(set(info.values()))  # 注意重复值的影响
        result = []
        fre.sort(reverse=True)
        print(fre)
        print(info)
        for v in fre:
            key = list(filter(lambda x: info[x]==v, info.keys()))
            result.extend(key)

        return result[:k]
# a=Solution22()
# print(a.topKFrequent(nums=[3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))
############################# 第3题 #################################

class Solution33:
    def sortColors(self, nums):
        info = {}
        for ele in nums:
            if ele not in info.keys():
                info[ele] = 1
            else:
                info[ele] += 1
        result = []
        js = []

        for key in  info.keys():
            pos = len(js)
            for i in range(len(js)):
                if key < js[i]:
                    pos = i
                    break
            js.insert(pos, key)
        #     print("haha: ",js)
        # print("here: ", info)
        for key in js:
            result.extend([key]*info[key])
            # print("last: ", result)

        return result

# a = Solution33()
# print(a.sortColors([0,1,2,0,2,2,2,0,0,2]))

class Solution333:
    def sortColors(self, nums):
        """[101202]"""
        cnts = [0] * 3
        for num in nums:
            cnts[num] += 1

        i = 0
        for color in range(3):
            for j in range(cnts[color]):
                nums[i] = color
                i += 1
        return nums

# a = Solution333()
# print(a.sortColors([0,1,2,0,2,2,2,0,0,2]))
################################################################################
class Solution4:
    def findContentChildren(self, g, s):
        # 左列表倒排

        anti = []
        for ele in g:
            pos = len(anti)
            for i in range(len(anti)):
                if ele > anti[i]:
                    pos = i
                    break
            anti.insert(pos, ele)

        # print("anti: ", anti)

        flag = 0
        for r in s:
            print("当前是：", r)
            for ele in anti:
                if r >= ele:
                    anti.remove(ele)
                    flag += 1
                    print("有")
                    break
        return flag


a = Solution4()
print(a.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))


