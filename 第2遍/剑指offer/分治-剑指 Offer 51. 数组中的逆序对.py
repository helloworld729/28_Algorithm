class Solution:
    def reversePairs(self, nums) -> int:
        # 将数组升序排列,超时
        cur_len = 0
        ll = len(nums)
        inverse = 0
        for i in range(ll):
            change_count = 0
            j = i
            cur_len += 1
            while j-1 >= 0 and nums[j] < nums[j-1]:
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp
                change_count += 1
                j -= 1
            inverse += change_count
        return inverse

    def reversePairs2(self, nums) -> int:
        """利用分治的思想，整体的逆序对=左半边的逆序对+右半边的逆序对+跨越两边的逆序对"""
        """时间复杂度0(nlgn)也就是归并排序， 空间复杂度O(N)创建等长辅助数组"""
        def merge(lst, left, middle, right):
            reverse_num = 0
            l_len, r_len = middle-left+1, right-middle
            l, r = lst[left: middle+1], lst[middle+1: right+1]
            i, j = 0, 0
            k = left
            while i <= l_len-1 and j <= r_len-1:
                if r[j] < l[i]:
                    lst[k] = r[j]
                    reverse_num += l_len-i
                    j += 1
                else:
                    lst[k] = l[i]
                    i += 1
                k += 1
            while i <= l_len-1:  # 假如右侧被清空
                lst[k] = l[i]
                i += 1
                k += 1

            while j <= r_len-1:
                lst[k] = r[j]
                j += 1
                k += 1

            return reverse_num

        def get_reverse_pairs(lst, left, right):
            if left >= right: return 0
            middle = left + (right-left) // 2
            l_num = get_reverse_pairs(lst, left, middle)
            r_num = get_reverse_pairs(lst, middle+1, right)
            crose_num = merge(lst, left, middle, right)
            return l_num+r_num+crose_num
        return get_reverse_pairs(nums, 0, len(nums)-1)

a = Solution()
lst = [5, 4, 3, 2, 1]
print(a.reversePairs2(lst))

