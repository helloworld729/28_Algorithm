def findPeakElement(nums) -> int:
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l

nums = [1]
print(findPeakElement(nums))