def fourSum(nums, target: int):
    nums.sort()
    ll = len(nums)
    res = []
    for first in range(ll - 4 + 1):
        if first > 0 and nums[first] == nums[first-1]: continue
        for second in range(first + 1, ll - 3 + 1):
            if second > 1 and nums[second] == nums[second-1] and second - 1 != first:continue
            temp_target = target - nums[first] - nums[second]
            i, j = second + 1, ll - 1
            while i < j:
                temp_sum = nums[i] + nums[j]
                if temp_sum < temp_target:  # 向右推进
                    while nums[i] + nums[j] < temp_target and i < j: i += 1
                elif temp_sum > temp_target:  # 向左推进
                    while nums[i] + nums[j] > temp_target and i < j: j -= 1
                else:
                    res.append([nums[first], nums[second], nums[i], nums[j]])
                    while nums[i] + nums[j] == temp_target and i < j: i += 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
target = -1
print(fourSum(nums, target))

