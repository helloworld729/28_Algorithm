from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        def get_pos(inter, target, pos):
            l, r = 0, len(inter)
            while l < r:
                mid = l + (r - l) // 2
                if inter[mid][pos] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        def merge(temp):
            """三元组融合"""
            nums = []
            res = []
            for pair in temp:
                nums.append([pair[0], "s"])
                nums.append([pair[1], "e"])
            nums.sort(key=lambda x: x[0])
            st = []
            for i in range(6):  # len(nums)
                if nums[i][1] == "s":
                    st.append(i)
                else:
                    start = st.pop()
                    if not st:
                        # 边界相同
                        if res and res[-1][1] == nums[start][0]:
                            res.append([res[-1][0], nums[i][0]])
                            res.pop(-2)
                        else:
                            res.append([nums[start][0], nums[i][0]])
            return res

        if not intervals or not intervals[0]: return [newInterval]
        a, b = newInterval
        left = max(get_pos(intervals, a, 0)-1, 0)
        right = min(get_pos(intervals, b, 1), len(intervals)-1)
        temp = merge([intervals[left], [a, b], intervals[right]])
        return intervals[:left] + temp + intervals[right+1:]


old = [[7,8]]
new = [4, 6]
a = Solution()
print(a.insert(old, new))


"""
时间复杂度：O(lgN)
空间复杂度：O(1)  

思路：用二分查找求出新区间的左右边界，获取3段候选区间，然后调用merge函数融合
      最后将融合后的结果拼接到无关区域即可
边界说明：例如在用二分法求左边界的过程：一般情形下，插入的位置左边的值比自己小
      右边比自己大，实际需要考虑的小list为intervals[left-1],所以需要用max处理
      同理，右边界需要用min处理。
"""

