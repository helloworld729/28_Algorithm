# ###################### 不同优先级表达式求值 leetcode-241 #####################################
def diffcal(input:'str'):
    return_list = []
    for index in range(len(input)):
        if input[index] in ['+', '-', '*']:
            left = diffcal(input[:index])
            right = diffcal(input[index+1:])

            for l in left:
                for r in right:
                    if input[index] == '+':
                        return_list.append(l + r)
                    elif input[index] == '-':
                        return_list.append(l - r)
                    else:
                        return_list.append(l * r)
    if not return_list:  # 当只是一个数，没有运算符
        return_list.append(int(input))
    return return_list
# print(diffcal("2*3-4*5"))


# ##################################### 简单计算器 ##########################################
def evaluate_expr(stack):  # )3+2
    res = stack.pop() if stack else 0  # 再次反转

    # Evaluate the expression till we get corresponding ')'
    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res

def calculate(s: str) -> int:

    stack = []
    n, operand = 0, 0  # 幂，操作数

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]

        if ch.isdigit():

            # Forming the operand - in reverse order.
            operand = (10**n * int(ch)) + operand
            n += 1

        elif ch != " ":
            if n:
                # Save the operand on the stack
                # As we encounter some non-digit.
                stack.append(operand)  # 操作数入栈
                n, operand = 0, 0

            if ch == '(':
                res = evaluate_expr(stack)
                stack.pop()

                # Append the evaluated result to the stack.
                # This result could be of a sub-expression within the parenthesis.
                stack.append(res)

            # For other non-digits just push onto the stack.
            else:
                stack.append(ch)

    # Push the last operand to stack, if any.
    if n:
        stack.append(operand)

    # Evaluate any left overs in the stack.
    return evaluate_expr(stack)
# print(calculate('1-2+3'))

# #################################最大子序和53 ############################################
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

分解为3个子问题
将序列分为左半边（含中值），右半边（不含中值），跨越两边（左元可选+中值+至少一个右元）
为什么左半边必须含有中值：假如最大子序列为中值及其左边所有元素，跨越和右分量均取不到，所以保证左可以取到
"""
def cross_sum(nums, left, right, p):
    if left == right:
        return nums[left]

    left_subsum = float('-inf')
    curr_sum = 0
    for i in range(p, left - 1, -1):
        curr_sum += nums[i]  # 一直在加，但和不一定上升
        left_subsum = max(left_subsum, curr_sum)

    right_subsum = float('-inf')
    curr_sum = 0
    for i in range(p + 1, right + 1):
        curr_sum += nums[i]
        right_subsum = max(right_subsum, curr_sum)

    return left_subsum + right_subsum

# print(cross_sum([0,1,2],0, 2, 1))
def helper(nums, left, right):  # 左右边界都可以取到
    if left == right:
        return nums[left]

    p = (left + right) // 2

    left_sum = helper(nums, left, p)
    right_sum = helper(nums, p + 1, right)
    cross_s = cross_sum(nums, left, right, p)

    return max(left_sum, right_sum, cross_s)
# print(helper([0,1,2],0, 2))
def maxSubArray(nums):
    return helper(nums, 0, len(nums) - 1)
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# 动规解法 还是动规简单
class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [nums[0]] * len(nums)
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

# ############################# 搜索二维矩阵 leetcode-240 ###################################
def searchMatrix(matrix, target):
    """右下增大
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    def bin_search(lst, target):
        l, r = 0, len(lst) - 1
        while l < r:
            mid = (l + r) // 2
            if lst[mid] == target:
                return True
            if lst[mid] < target:
                l = mid
            else:
                r = mid
            if l + 1 == r:
                return lst[0] == target or lst[len(lst) - 1] == target
        return lst[0] == target  # 当矩阵长度为1时，直接到这里

    for i in matrix:
        if i[-1] < target or i[0] > target:
            continue
        if bin_search(i, target):
            return True
    return False

# ############################# 选择合适起点 leetcode-240 ###################################
def searchMatrix2(self, matrix, target):
    """从左下开始，大于目标值上移，小于目标值右移"""
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    height = len(matrix)
    width = len(matrix[0])
    row = height - 1
    col = 0
    while col < width and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:  # found it
            return True
    return False

# ############################# 矩阵切分 leetcode-240 ###################################
def searchMatrix3(matrix, target):
    # an empty matrix obviously does not contain `target`
    if not matrix:
        return False
    def search_rec(left, up, right, down):
        # this submatrix has no height or no width.
        if left > right or up > down:
            return False
        # `target` is already larger than the largest element or smaller
        # than the smallest element in this submatrix.
        elif target < matrix[up][left] or target > matrix[down][right]:
            return False
        mid = left + (right - left) // 2
        # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        row = up
        while row <= down and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1
        return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)
    return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


# ############################# 乘积最大连续子数组 leetcode-152 ###################################
def cross_mul(nums, l, r, mid):
    if nums[mid] == 0:
        return 0
    curr_l = curr_r = 1
    max_l = max_r = float('-inf')
    min_l = min_r = float('inf')
    for i in range(mid, l-1, -1):
        curr_l = curr_l * nums[i]
        max_l = max(max_l, curr_l)
    for j in range(mid, r+1, 1):
        min_l = min(min_l, curr_l)
        curr_r = curr_r * nums[j]
        max_r = max(max_r, curr_r)
        min_r = min(min_r, curr_r)
    return max(min_l * min_r//nums[mid], min_l * max_r//nums[mid],
               max_l * max_r//nums[mid], max_l * min_r//nums[mid])
print(cross_mul([2,-3,4,-2], 0, 3, 1))

def maxPro(nums, l, r) -> int:
    mid = l + (r-l)//2
    if l == r:
        return nums[l]
    return max(maxPro(nums, l, mid), maxPro(nums, mid+1, r), cross_mul(nums, l, r, mid))
# print(maxPro([2,-3,4,-2], 0, 3))

