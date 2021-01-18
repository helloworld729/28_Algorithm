# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/17 13:33

nums = [10,9,2,5,3,7,101,18]
def maxAsc(nums):
    length = len(nums)

    dpLeft = [1] * length
    cansLeft = [[nums[i]] for i in range(length)]
    for i in range(length):
        for j in range(i):
            if nums[i] > nums[j] and dpLeft[i] < dpLeft[j] + 1:
                dpLeft[i] = dpLeft[j] + 1
                cansLeft[i] = cansLeft[j] + [nums[i]]

    dpRight = [1] * length
    cansRight = [[nums[i]] for i in range(length)]
    for i in range(length-1, -1, -1):
        for j in range(length-1, i, -1):
            if nums[i] > nums[j] and dpRight[i] < dpRight[j] + 1:
                dpRight[i] = dpRight[j] + 1
                cansRight[i] = [nums[i]] + cansRight[j]

    index = maxLen = 0
    for i in range(length):
        if dpLeft[i] + dpRight[i] > maxLen:
            index, maxLen = i, dpLeft[i] + dpRight[i]
            
    print(maxLen)
    print(cansLeft)
    print(cansRight)
    print(cansLeft[index][:-1] + cansRight[index])

maxAsc(nums)

