class Solution:
    """快排双指针思路"""
    def exchange(self, lst):
        if not lst: return lst
        l, r = 0, len(lst)-1
        pivot = lst[l]
        while l < r:
            while l < r and lst[r] % 2 == 0:  # odd
                r -= 1
            if l < r:
                lst[l] = lst[r]
                l += 1
            while l < r and lst[l] % 2 == 1:
                l += 1
            if l < r:
                lst[r] = lst[l]
                r -= 1
        lst[l] = pivot
        return lst

lst = [1, 2, 3, 4]
a = Solution()

print(a.exchange(lst))

