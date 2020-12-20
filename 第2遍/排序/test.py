def mergesort(lst, left, right):
    def merge(lst, left, middle, right):
        cans = list()
        i, j = left, middle+1  # 定义指针起点
        while i <= middle or j <= right:
            if j > right or i <= middle and lst[i] <= lst[j]:
                cans.append(lst[i])
                i += 1
            elif i > middle or j <= right and lst[i] > lst[j]:
                cans.append(lst[j])
                j += 1
        lst[left: right+1] = cans

    if left >= right: return
    middle = left + (right-left)//2
    mergesort(lst, left, middle)
    mergesort(lst, middle+1, right)
    merge(lst, left, middle, right)

lst = [1, 2, 4, 3, 6, 5, 8, 7, 0]
mergesort(lst, 0, len(lst)-1)
print(lst)

