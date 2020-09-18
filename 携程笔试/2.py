(r,c) = list(map(int, input().split()))
def construct(row, cline):
    grid = [[0 for _ in range(cline)] for _ in range(row)]
    cur_num = 1
    i = 0
    while i <= row-1:  # 定左边第一个元素
        r, c = i, 0
        while r >= 0 and c <= cline-1:
            grid[r][c] = cur_num
            r -= 1
            c += 1
            cur_num += 1
        i += 1
    j = 1
    while j <= cline:
        r, c = row - 1, j
        while c <= cline-1:
            grid[r][c] = cur_num
            r -= 1
            c += 1
            cur_num += 1
        j += 1
    return grid

def get_result(nums):
    res = []
    for data in nums:
        res.append(data)
    return res

for data in get_result(construct(row=r, cline=c)):
    print(data)