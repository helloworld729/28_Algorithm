## 一、对撞指针-两数之和

**题目**<br>
给定一个已按照**升序排列** 的有序数组，找到两个数使得它们相加之和等于目标数。<br>

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。<br>

__说明__:<br>
返回的下标值（index1 和 index2）不是从零开始的。<br>
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。<br>

**示例:**<br>
输入: numbers = [2, 7, 11, 15], target = 9<br>
输出: [1,2]<br>
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。<br>

来源：力扣167（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted<br>

**知识点**<br>
对撞指针用于遍历数组，当数组已经是有序的情况下，用两个指针分别指向最大和最小的元素<br>
然后协同移动，完成所需的任务。<br>

**<font color=#FF0000>思路:</font>**<br>
1、当和大于target时：左移大指针<br>
2、当和小于target时：右移小指针<br>
3、没有解返回None


```python
def twoSum(numbers, target):
    """nums=[2,7,11,15]"""
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l, r]
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
    return None       
    
```

测试：


```python
twoSum([2,7,11,15], 26)
```




    [2, 3]



## 二、快排

**题目**<br>
在未排序的数组中找到** 第k 个最大的元素**。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。<br>

**示例:**<br>

输入: [3,2,1,5,6,4] 和 k = 2<br>
输出: 5<br>

来源：力扣215（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array<br>

**知识点**<br>
1、pivot：每次排序选择的基本元素，可以是第一个或者随机<br>
2、partition：一次遍历称作一次partition<br>
3、利用双指针配合操作<br>
**思路**<br>
如果不需要全部排序可以根据具体情况，对单侧排序


```python
def q_sort(lst, l, r):
    """
    快速排序
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :return:
    """
    if l >= r:  # 边界条件，只有一个元素
        return

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:    # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止, 第一个条件保证第一个数最小时数组不会越界
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置
    
    q_sort(lst, l, i-1)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面
    q_sort(lst, i+1, r)  # 递归推进，右侧快排，

    return lst
```


```python
q_sort([3,5,6,4], 0, 3)
```




    [3, 4, 5, 6]




```python
def q_sort(lst,k):
    """
    基于切片的第K大，递归时是全新的变量
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :param k: 返回第K大的元素，如果pivot位置在k右边，那么右边的部分不用继续排序
    :return:
    """
    if k <= 0:
        return None
    l, r = 0, len(lst) - 1
    if l >= r:  # 边界条件，只有一个元素
        return lst[l]

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:    # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止, 第一个条件保证第一个数最小时数组不会越界
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置
    
    if i == k-1:
        return lst[i]
    elif i < k-1:
        return q_sort(lst[i+1:], k-i-1)  # 递归推进，右侧快排，
    elif i > k-1:
        return q_sort(lst[l: i], k)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面    
```


```python
q_sort([3,5,6,4],3)
```




    5




```python
def q_sort(lst, l, r, k):
    """
    基于边界的第K大，减少变量使用
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :param k: 返回第K大的元素，如果pivot位置在k右边，那么右边的部分不用继续排序
    :return:
    """
    if k <= 0:
        return None
    if k > len(lst):
        k = len(lst)
    
    if l >= r:  # 边界条件，只有一个元素
        return lst[r]

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:    # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止, 第一个条件保证第一个数最小时数组不会越界
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置
    
    if i == k-1:
        return lst[i]
    elif i < k-1:
        return q_sort(lst, i+1, r, k-i)  # 递归推进，右侧快排，
    elif i > k-1:
        return q_sort(lst, l, i-1, k)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面    
```


```python
q_sort([3,5,6,4],0, 3, 5)  # 5
```




    6



## 三、荷兰国旗

**题目**
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，**原地对它们进行排序**，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

**注意:**
不能使用代码库中的排序函数来解决这道题。

**示例:**

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

来源：力扣75（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors

**思路1**<br>
1、计数<br>
2、原地重写数组<br>

**思路2**<br>
三向切分快排：选择1作为pivot，遇到0排到左边，遇到2排到右边<br>
now的左边肯定没有2，因为遇到2就跑到了后面，tail回退一步；<br>
now的左边保证为0/1，遇到1pass，遇到0就抛到head；<br>
now步进时机：遇到0并且和head交换后、遇到1<br>
note：head和now分开后，head肯定不会指向0


```python
class Solution1:
    def sortColors(self, nums):
        cnts = [0]*3  # 3是颜色的数目
        for i in nums:
            cnts[i] += 1 # 完成计数

        j = 0
        for i in range(3):  # 3是颜色的数目
            for k in range(cnts[i]):  # 某颜色的数目
                nums[j] = i
                j += 1
        return nums
```


```python
a = Solution1()
print(a.sortColors([2,0,2,1,1,0]))
```

    [0, 0, 1, 1, 2, 2]
    


```python
class Solution2:
    def sortColors(self, nums):
        head, now, tail = 0, 0, len(nums)-1
        while now <= tail:  # 注意等于号否则【1，0，2】通过不了
            if nums[now] == 2:  # 只有遇到2交换后才修改tail
                nums[now], nums[tail] = nums[tail], nums[now]
                tail -= 1 
                print(nums)
                
            elif nums[now] == 0:  # 只有遇到0交换后才修改head
                nums[now], nums[head] = nums[head], nums[now]
                head += 1
                now += 1  # now 必须在head的右侧
                print(nums)
            
            else:  
                now += 1  # 每一次操作要么tail减小，要么now增加，故一定会停止
                
        return nums
```


```python
a = Solution2()
print(a.sortColors([2,1,2,0,1]))
```

    [1, 1, 2, 0, 2]
    [1, 1, 0, 2, 2]
    [0, 1, 1, 2, 2]
    [0, 1, 1, 2, 2]
    

## 四、贪心

**题目**：<br>
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子**最多只能给一块**饼干。<br>
对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，<br>
都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。<br>
你的目标是尽可能**满足越多数量**的孩子，并输出这个最大数值。<br>

**注意**：<br>

你可以假设胃口值为正。<br>
一个小朋友最多只能拥有一块饼干。<br>

**示例** 1:<br>

输入: [1,2,3], [1,1]<br>

输出: 1<br>

**解释:** <br>
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。<br>
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。<br>
所以你应该输出1。<br>

来源：力扣455（LeetCode）
链接：https://leetcode-cn.com/problems/assign-cookies<br>

**思路:** <br>


```python
class Solution:
    def findContentChildren(self, g, s):  # g是胃口，s是饼干
        g, s = sorted(g), sorted(s)  # 正排        
        cnts_g, cnts_s = 0, 0  # 等待满足的胃口索引， 当前饼干索引
        
        while cnts_g < len(g) and cnts_s < len(s):
            if g[cnts_g] <= s[cnts_s]:
                cnts_g += 1
            cnts_s += 1
        return cnts_g        
```


```python
a = Solution()
print(a.findContentChildren([1,2,3], [1,1]))
```

    1
    


```python

```
