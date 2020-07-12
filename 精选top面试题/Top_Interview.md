**面试题 16.06. 最小差**<br>
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差<br>
示例：<br>
输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}<br>
输出： 3，即数值对(11, 8)<br>
思路1：排序 + 二分 nlogn
思路2：排序 + 双指针 nlogn


```python
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        b.sort()  # nlogn
        ret = abs(a[0]-b[0])
        for i in a: # nlogn
            index = bisect.bisect(b, i)
            if index == 0:
                ret = min(ret, abs(i-b[0]))
            elif index == len(b):
                ret = min(ret, abs(i-b[-1]))
            else:
                ret = min(ret, abs(i-b[index]), abs(i-b[index-1]))   
        return ret
```


```python
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()  # nlogn
        i = j = 0
        ret = abs(a[0]-b[0])
        while i < len(a) and j < len(b):
            ret = min(ret, abs(a[i]-b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ret
```


```python

```

**56. 合并区间**<br>
给出一个区间的集合，请合并所有重叠的区间。<br>
示例 1:<br>
输入: [[1,3],[2,6],[8,10],[15,18]]<br>
输出: [[1,6],[8,10],[15,18]]<br>
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].<br>
示例 2:<br>
输入: [[1,4],[4,5]]<br>
输出: [[1,5]]<br>
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。<br>
通过次数72,050提交次数174,657<br>

**知识点：列表排序**<br>
a = [[8,10],[1,3],[2,6],[15,18]]<br>
a.sort(key=lambda x: x[0])  # 此处的x就是每一个区间元素，默认用首元素排序，此处可以不写<br>


```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()  # 按照首元素升序排列
        merged = []
        merged.append(intervals[0])
        for lst in intervals[1:]:
            if lst[0] > merged[-1][1]:
                merged.append(lst)
            else:
                merged[-1][1] = max(lst[1], merged[-1][1])
        return merged
```

**1. 两数之和**<br>
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。<br>
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 <br>
示例:<br>
给定 nums = [2, 7, 11, 15], target = 9<br>
因为 nums[0] + nums[1] = 2 + 7 = 9<br>
所以返回 [0, 1]<br>
**方法1知识点**：列表排序，反求索引，列表重复值不同索引 NlogN<br>
**方法2知识点**：利用哈希表记录元素和索引，然后直接查target-当前值是否在dict中。O(N)O(N)


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = sorted(nums)
        l, r = 0, len(lst)-1
        
        while l < r:
            if lst[l] + lst[r] == target:
                if lst[l] == lst[r]:
                    res = [x for x in range(len(nums)) if nums[x] == lst[l]]  # 重复值索引
                    return res[:2]
                else:
                    return [nums.index(lst[l]), nums.index(lst[r])]
            elif lst[l] + lst[r] < target:
                l += 1
            else:
                r -= 1
```


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        back_dict = {}

        for i in range(len(nums)):  # 记录数值和索引
            if back_dict.get(nums[i], -1) == -1:
                back_dict[nums[i]] = [i]
            else:
                back_dict[nums[i]].append(i)
        # print(back_dict)
        for num in nums:  # 可以归并到上面的循环中
            if back_dict.get(target - num, -1) == -1:  # 差值不在字典中
                continue
            elif num != target-num:  # 差值在字典中，而且两个加数不等
                print(num, 'here')
                return [back_dict[num][0], back_dict[target-num][0]]
            elif len(back_dict[num]) > 1:  # 两个加数相等
                return [back_dict[num][0], back_dict[num][1]]
```


```python

```

**2. 两数相加**<br>
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。<br>
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。<br>
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。<br>
示例：<br>
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)<br>
输出：7 -> 0 -> 8<br>
原因：342 + 465 = 807<br>
**知识点：链表**。**亮点**：root的首元素实际上没有意义，只是为了开创，返回从next开始，好处是避免头部进位的讨论，简化代码。<br>
**解惑**：链表赋值类似于list，数值是共享的,内存也是共享的。就是别名而已。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = ListNode(0)
        temp = root

        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            s = (a+b+carry) % 10
            carry = (a+b+carry) // 10
            node = ListNode(s)
            temp.next = node
            temp = node            
            
        if carry != 0:
            node = ListNode(carry)
            temp.next = node
                    
        return root.next
```


```python

```

**3. 无重复字符的最长子串**<br>
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。<br>
示例 1:<br>
输入: "abcabcbb"<br>
输出: 3 <br>
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。<br>
**思路1**：方法一采用了动规的方法：状态转移：如果当前字符不在前一字符所在的窗口，则max加一，否则在前一窗口找到当前char的索引截断。<br>
**思路2**：方法一种需要判断char是否在某个子字符串中，造成复杂度增加，考虑用哈希表和一个ignore抵达索引来换取时间。<br>


```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = ret = 1
        for i in range(1, len(s)):
            if s[i] in s[i-res: i]:  # res当前子串长度，ret最长子串长度
                res = res - (1+ s[i-res: i].index(s[i])) + 1                
            else:
                res += 1
                ret = max(ret, res)
        return ret
```


```python
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        ignore_str_index_end = -1
        dic = {}        
        max_length = 0  

        for i, c in enumerate(s):
            # 索引都会大于等于0，新字符的索引为-1，否则为已经出现
            # 第二个条件是因为ignore机制已经截断了重复char以及之前的char
            if c in dic and dic[c] > ignore_str_index_end:
                ignore_str_index_end = dic[c]  # 求出索引，无效推进
                dic[c] = i
            else:
                dic[c] = i
                max_length = max(i - ignore_str_index_end, max_length)  # 当前子串长度、最长长度
        return max_length
```


```python

```

**7. 整数反转**
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。<br>
示例 1:输入: 123 输出: 321<br>
示例 2:输入: -123输出: -321<br>
示例 3:输入: 120 输出: 21<br>
注意:<br>
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。<br>



```python
class Solution:
    def reverse(self, x: int) -> int:           
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //= 10
        return res if x >0 else -res
```




    3



**14. 最长公共前缀**<br>
编写一个函数来查找字符串数组中的最长公共前缀。<br>
如果不存在公共前缀，返回空字符串 ""。<br>
示例 1:<br>
输入: ["flower","flow","flight"]<br>输出: "fl"<br>
示例 2:<br>
输入: ["dog","racecar","car"]<br>输出: ""<br>
解释: 输入不存在公共前缀。<br>
思路1：逐个单词比较(推荐)<br>
思路二：逐个index比较<br>


```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        s = strs[0]  # 第一个单词
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0 :  # 只有是公共前缀才会返回0，否则返回索引或者-1
                s = s[:-1]
            if len(s) == 0:
                break
        return s
```


```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        strs.sort(key=len)
        flag, i = False, 0
        for i in range(0, len(strs[0])):  # 不同index
            for j in range(1,len(strs)):  # 不同单词
                if strs[j][i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                i -= 1
                break

        return strs[0][:i+1]

```


```python

```

**15. 三数之和**<br>
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。<br>
注意：答案中不可以包含重复的三元组。<br>

示例：<br>
给定数组 nums = [-1, 0, 1, 2, -1, -4]，<br>
满足要求的三元组集合为：<br>
[<br>
  [-1, 0, 1],<br>
  [-1, -1, 2]<br>
]<br>

算法流程：<br>
1特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。<br>
2对数组进行排序。<br>
3遍历排序后数组：<br>
&#8195;&#8195;&#8195;若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。<br>
&#8195;&#8195;&#8195;对于重复元素：跳过，避免出现重复解<br>
&#8195;&#8195;&#8195;令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：<br>
&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;当 nums[i]+nums[L]+nums[R]==0，循环，判断左界和右界是否和下一位置重复，<br>
&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;去除重复解。并同时将 L,R移到下一位置，寻找新的解<br>
&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;若和大于 0，说明 nums[R] 太大，R 左移<br>
&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;若和小于 0，说明 nums[L] 太小，L 右移<br>


```python
class Solution:  # 1000ms
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):  # 重复元素构成的解在前面已经考虑过了
                continue
            L, R = i + 1, n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    L = bisect.bisect_right(nums, nums[L])  # 去除重复值
                    R = bisect.bisect_left(nums, nums[R])
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res
```


```python
class Solution:  # 100ms
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        nums = sorted(counts)  # key排序
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num * 2 in counts:
                        ans.append([num, num, -2 * num])
            if num < 0: # sum 才有可能为0
                two_sum = -num
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                for i in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    j = two_sum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])
        return ans
```


```python
a = {2:'ll', 1:'pp'}
a = sorted(a)
a
```




    [1, 2]




```python
# 如果不用去重的话，可以用分治
def fun(l, r, num, lst, target=0):
    if num == 1:  # 边界条件
        for k in range(l, r+1):  # 确保r可以取到
            if lst[k] == target:
                return [lst[k]]
        return []
    res = []
    for i in range(l, r+1):
        rest = fun(i+1, r, num-1, lst, target=target-lst[i])
        for cans in rest:
            res.append([cans] + [lst[i]]) if isinstance(cans, int) else res.append(cans + [lst[i]])
    return res
```


```python

```

**17. 电话号码的字母组合**<br>
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。<br>
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。<br>
示例:<br>
输入："23"<br>
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].<br>
说明:<br>
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。<br>
思路：分治


```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        back_dic = {
        '2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z'],
        }

        def combine(lst1, lst2):
            res = []
            for i in lst1:
                for j in lst2:
                    res.append(i+j)
            return res

        def for_ward(l=0):
            if l == len(digits)-1:
                return back_dic[digits[l]]
            return combine(back_dic[digits[l]], for_ward(l+1))

        return for_ward()
        
```


```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        back_dic = {
                        '2':['a', 'b', 'c'],
                        '3':['d', 'e', 'f'],
                        '4':['g', 'h', 'i'],
                        '5':['j', 'k', 'l'],
                        '6':['m', 'n', 'o'],
                        '7':['p', 'q', 'r', 's'],
                        '8':['t', 'u', 'v'],
                        '9':['w', 'x', 'y', 'z'],
                    }
        global res
        res = back_dic[digits[0]]

        def combine(lst1, lst2):
            ret = []
            for i in lst1:
                for j in lst2:
                    ret.append(i+j)
            return ret

        def for_ward(l=1):
            if l == len(digits):
                return
            global res
            res = combine(res, back_dic[digits[l]])
            for_ward(l + 1)
        for_ward()
        return res
```


```python

```

**26. 删除排序数组中的重复项**<br>
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。<br>
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。<br>
示例 1:<br>
给定数组 nums = [1,1,2], <br>
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 <br>
你不需要考虑数组中超出新长度后面的元素。<br>
知识点：双指针


```python
class Solution:
    def removeDuplicates(self, nums) -> int:
        l = len(nums)
        if l < 2:
            return l
        now = left = count = 0
        while now < l:
            while now < l and nums[now]==nums[left]:
                now += 1

            if now < l:
                nums[left + 1] = nums[now]
                left += 1  # 每次移动之后两指针数据相同，保证now步进
                count += 1
        return count + 1
```


```python

```

**34. 在排序数组中查找元素的第一个和最后一个位置**<br>
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。<br>
你的算法时间复杂度必须是 O(log n) 级别。<br>
如果数组中不存在目标值，返回 [-1, -1]。<br>
示例 1:<br>
输入: nums = [5,7,7,8,8,10], target = 8<br>
输出: [3,4]<br>
示例 2:<br>
输入: nums = [5,7,7,8,8,10], target = 6<br>
输出: [-1,-1]<br>
**思路：二分**


```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:  # mid 就是目标值，这一块亦可以直接用bisect
                while nums[l] != target:
                    if nums[l] < nums[mid]:
                        l += 1
                    if nums[l] == nums[mid]:
                        break

                while nums[r] != target:
                    if nums[r] > nums[mid]:
                        r -= 1
                    if nums[r] == nums[mid]:
                        break
                return [l, r]

            if l + 1 == r or l == r :  # 当目标值小于target 会出现第二种情况,当然也可以合并到开始作为特例：【2,2】-1
                if nums[r] == target:
                    return [r, r]
                if nums[l] == target:
                    return  [l, l]
                else:
                    return [-1, -1]
```


```python
class Solution:  # 掉包方法
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target) > 0:
            l = bisect.bisect_left(nums, target)
            r = bisect.bisect_right(nums, target)
            return [l, r-1] 
        else:
            return [-1, -1]
```


```python

```

**179. 最大数**
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。<br>-
示例 1:<br>
输入: [10,2]<br>
输出: 210<br>
示例 2:<br>
输入: [3,30,34,5,9]<br>
输出: 9534330<br>
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。<br>
思路：转化为字符串后，对字符串排序，排序时间复杂度nlgn


```python
class LargerNumKey(str):  # 不能用lambda代替，因为
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```

**162. 寻找峰值**<br>
峰值元素是指其值大于左右相邻值的元素。<br>
给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。<br>
数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。<br>
**你可以假设 nums[-1] = nums[n] = -∞。**<br>
示例 1:<br>
输入: nums = [1,0,3,1]<br>
输出: 0<br>
解释: 1 是峰值元素，你的函数应该返回其索引 0。<br>
示例 2:<br>
输入: nums = [1,2,1,3,5,6,4]<br>
输出: 1 或 5 <br>
解释: 你的函数可以返回索引 1，其峰值元素为 2；<br>
     或者返回索引 5， 其峰值元素为 6。<br>
说明:<br>

你的解法应该是 O(logN) 时间复杂度的。<br>
思路：根据复杂度，可以确定用二分法，机制可以类比斜率和极值点。


```python
class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums)-1 
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1  # 很好
        return l
```




    0.0




```python

```

**200. 岛屿数量**<br>
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，<br>
并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。<br>
可以把岛屿看做集中连片的1。示例 1:<br>
输入:<br>
1 1 1 1 0<br>
1 1 0 1 0<br>
1 1 0 0 0<br>
0 0 0 0 0<br>
输出: 1<br>


```python
# 方法1深度优先搜索
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0  # 记忆搜索将格点标记位0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":  # 只要出现了1，必定对应一个岛屿
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands
```


```python
# 方法2：广度优先搜索 用队列迭代替代递归
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        
        return num_islands
```


```python
# 方法3：并查集https://zhuanlan.zhihu.com/p/93647900
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1  # 合并一次，岛屿数目减1
    
    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)  # 初始化
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)  # 合并算法
        
        return uf.getCount()
```


```python

```

**395. 至少有K个重复字符的最长子串**<br>
题目：找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。<br>
示例 2:<br>
输入:s = "ababbc", k = 2  输出:5<br>
最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。<br>
思路1：分治<br>


```python
class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                # 满足分割条件，进行分割
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)
```


```python

```

**287. 寻找重复数**
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。<br>
示例 2:输入: [3,1,3,4,2]输出: 3<br>
说明：<br>
不能更改原数组（假设数组是只读的）。<br>
只能使用额外的 O(1) 的空间。<br>
时间复杂度小于 O(n2) 。<br>
数组中只有一个重复的数字，但它可能不止重复出现一次。<br>
思路1：快排<br>
时间复杂度：O(nlgn)。排序调用在 Python 和 Java 中花费 {O}(nlgn)O(nlgn) 时间，因此它支配后续的线性扫描。<br>
空间复杂度：O(1) or O(n)，在这里，我们对 nums 进行排序，因此内存大小是恒定的。如果我们不能修改输入数组，那么我们必须为 nums 的副本分配线性空间，并对其进行排序。<br>

思路2：快慢指针-循环检测<br>
快慢指针法, 兔子与乌龟同时在头节点出发, 兔子每次跑两个节点, 乌龟每次跑一个节点, 如果兔子能够追赶到乌龟, 则链表是有环的<br>
还是前面的龟兔赛跑, 当兔子追到乌龟的时候, 假设有另外一只乌龟从头节点开始往前爬, 每次也只爬一个节点, 那么两只乌龟会在入环的节点相遇<br>
结合141 142 题目:https://leetcode-cn.com/problems/find-the-duplicate-number/solution/qian-duan-ling-hun-hua-shi-tu-jie-kuai-man-zhi-z-3/<br>


```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
```


```python
def findDuplicate(nums) -> int:
    slow, fast = 0, 0
    # 慢指针走一步，快指针走两步
    slow, fast = nums[slow], nums[nums[fast]]
    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]
        
    before, after = 0, slow
    while before != after:
        before, after = nums[before], nums[after]
        
    return before
```


```python

```

**227. 基本计算器 II**<br>
实现一个基本的计算器来计算一个简单的字符串表达式的值。<br>

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。<br>

示例 :<br>
输入: " 3+5 / 2 "<br>
输出: 5<br>
说明：请不要使用内置的库函数 eval。<br>
思路：stack<br>
Note：//做除法的时候，对于float结果取一个较小的数，对于负数-3//2结果为-2值得注意。<br>


```python
def calculate(s):
    """思路：求每个符号对应的局部结果（加减直接入栈，乘除先弹出计算后再压入）"""
    """思路：遇到新的符号代表 数据已经准备好 计算前一局部"""
    part = []
    sign, num = '+', 0
    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            num = num * 10 + int(char)
        if char in '+-*/' or i == len(s) - 1:
            if sign == '+':
                part.append(num)
            elif sign == '-':
                part.append(-num)
            elif sign == '*':
                part.append(part.pop() * num)
            elif sign == '/':
                part.append(int(part.pop()/num))
            num = 0
            sign = char

    return sum(part)
```


```python

```

**238. 除自身以外数组的乘积**<br>
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。<br>
示例:输入: [1,2,3,4]输出: [24,12,8,6]<br>
思路：动规，求元素左边乘积和元素右边乘积，然后nums[i] = l[i-1] * r[i+1]


```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        for index in range(1, len(nums)):
            l[index] = l[index-1] * nums[index -1]
        for index in range(len(nums)-2, -1, -1):
            r[index] = r[index+1] * nums[index + 1]
        for index in range(len(nums)):
            nums[index] = l[index] * r[index]
        return nums
            
```


```python

```

**104. 二叉树的最大深度**<br>
给定一个二叉树，找出其**最大深度**。<br>
示例：<br>
给定二叉树 [3,9,20,null,null,15,7]，<br>
返回它的最大深度 3 。<br>
思路：子节点的深度比父节点 + 1


```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        que, dep = [], 0
        que.append((1, root))
        while que:
            curr_dep, node = que.pop()         
            if node:
                dep = max(dep, curr_dep)  
                que.append((curr_dep+1, node.left)) if node.left else ''
                que.append((curr_dep+1, node.right)) if node.right else ''
        return dep
```
