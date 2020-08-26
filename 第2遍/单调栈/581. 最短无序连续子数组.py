class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        ll = len(nums)
        l, r = ll-1, 0
        st = []
        for i in range(ll):
            if st and nums[st[-1]] > nums[i]:
                while st and nums[st[-1]] > nums[i]:
                    st.pop()
                l = min(l, st[-1]+1) if st else 0
            st.append(i)
        st = []
        for j in range(ll-1, -1, -1):
            if st and nums[st[-1]] < nums[j]:
                while st and nums[st[-1]] < nums[j]:
                    st.pop()
                r = max(r, st[-1]-1) if st else ll-1
            st.append(j)
        return r-l + 1


lst = [2,1]
a = Solution()
print(a.findUnsortedSubarray(lst))

"""
zuobianji e
"""