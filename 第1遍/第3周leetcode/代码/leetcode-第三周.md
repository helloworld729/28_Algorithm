## 一、求众数

**题目**：
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。<br>
你可以假设数组是非空的，并且给定的数组总是存在多数元素。 <br>
这里的众数和数学上出现次数最多的概念不一致，这里要求次数必须超过一半。<br>

**示例**:
输入: [2,2,1,1,1,2,2]
输出: 2<br>

来源：力扣169（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element<br>

思路：<br>
1、用多数投票算法：局部不是众数则整体不是众数<br>
2、直接排序求解


```python
class Solution:
    def majorityElement(self, nums):
        cnt, majority  = 0, nums[0]
        for num in nums:
            if cnt == 0:
                majority = num
            if majority == num:
                cnt += 1
            else:
                cnt -= 1
        return majority              
```


```python
a = Solution()
a.majorityElement([1,2,1,1,1,1,1,2,3,6,3])
```




    1




```python
class Solution2:
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[len(nums)//2]
```


```python
a = Solution2()
a.majorityElement([1,2,1,1,1,1,1,2,3,6,3])
```




    1



## 二、进制转换

**题目**
给定一个整数，将其转化为7进制，并以字符串形式输出。

**示例 1**:
输入: 100
输出: "202"<br>
**示例 2**:
输入: -7
输出: "-10"<br>
注意: 输入范围是 [-1e7, 1e7] 。

**思路**：
nums %7 确定本权位<br>
nums//7 确定高权位<br>
65/7  = 9...2 :65按7编组后，剩余2即7的0次对应；<br>
65//7 = 9 :除去余数后可以用9个7表示；<br>
9/7  = 1...2：假设现在有9组7，7个组成一组可以用更高位表示，剩下2个在本层表示。<br>
归纳：商表示高层，余数表示本层


```python
class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        is_neg = True if num < 0 else False
        if is_neg:
            num = -num
        ans =''
        if num > 0:
            while num > 0:
                ans += str(num%7)
                num //= 7
        ans = ans[::-1]
        if is_neg:
            ans = '-' + ans
        return ans
            
```


```python
a = Solution()
a.convertToBase7(65)
```




    '122'




```python

```

## 三、相遇问题

给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

来源：力扣462（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii<br>
知识点：典型的相遇问题，最小的移动次数为都移动到**中位数**，而**不是平均值**<br>
原因分析，假设a>m>b，那么a-b = a-m + (m-b),一个序列中，中位数一定存在<br>


```python
class Solution:
    def minMoves2(self, nums) -> int:
        nums = sorted(nums)
        res = 0
        i, j = 0, len(nums) - 1
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res
```


```python

```

## 四、最长回文串

**题目**<br>
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。<br>
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。<br>

注意:<br>
假设字符串的长度不会超过 1010。<br>

示例 1:<br>
输入:<br>
"abccccdd"<br>
输出:<br>
7<br>

解释:<br>
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。<br>

来源：力扣409（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindrome<br><br>
思路：哈希表(可以用count简化代码)


```python
from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        count = Counter(s) 
        couple = 0
        for nums in count.values():
            couple += nums//2
        
        if len(s) > 2*couple:
            return 2*couple + 1
        else:
            return len(s)
```


```python

```

## 五、数组和矩阵

**378. 有序矩阵中第K小的元素**<br>
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。<br>
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。<br>

 

示例:<br>

matrix = [<br>
   [ 1,  5,  9],<br>
   [10, 11, 13],<br>
   [12, 13, 15]<br>
],<br>
k = 8,<br>

返回 13。<br>
**思路：利用堆排序**：将一组或者一列数据入堆，然后依次抛出k个元素即可，这里没有采取把所有元素全部入堆<br>
而是根据需要的K入堆，每次抛出一个数据后，都会新加入一个数据，这个数据就是被抛出数据的下一个或者右一个，<br>
可以从全局的角度考虑原因。实际上这是一个优先队列


```python
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        h = []
        m, n = len(matrix), len(matrix[0])  # 行，列数目
        for i in range(m):  # 第一列入堆
            heapq.heappush(h, (matrix[i][0], i, 0))
        for i in range(k-1):
            item = heapq.heappop(h)
            r, c = item[1], item[2]
            if c < n-1:
                heapq.heappush(h, (matrix[r][c+1], r, c+1))
        return heapq.heappop(h)[0]
```


```python

```

## 六、位运算

**260. 只出现一次的数字 III**<br>
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。<br>

示例 :<br>

输入: [1,2,1,3,2,5]<br>
输出: [3,5]<br>
注意：<br>

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。<br>
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？<br>
**思路：利用位运算**<br>
知识点：任何数与0亦或为自身，任何数与自身亦或为0，通过以便扫描，确定两个single num的亦或值flag<br>
falg与反码相与，结果为flag最右侧的1保住，其他bits为0.基于此可以将原nums分为两组：该flag位为0或者1<br>
最后，由于两个single num分到了不同的组，各自一遍亦或就可以得到这两个数。<br>


```python
class Solution:
    def singleNumber(self, nums):
        flag = 0
        for num in nums:
            flag ^= num  # 到此为两个single num亦或的结果
        flag &= -flag  # 到此标记处最右侧的1

        res = [0, 0]
        for num in nums:  # 数据分组
            if flag & num == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
```


```python

```
