## 一、动态规划

递归和动态规划都是将原问题拆成多个子问题然后求解，他们之间最本质的区别是，动态规划保存了子问题的解，<br>
避免重复计算

**题目1**：<br>
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。<br>
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？<br>

**实例**：<br>
输入： 3
输出： 3<br>
解释： 有三种方法可以爬到楼顶。<br>
1.  1 阶 + 1 阶 + 1 阶<br>
2.  1 阶 + 2 阶<br>
3.  2 阶 + 1 阶<br>

来源：力扣70（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs<br>

**知识点**：斐波那契数 p = p1 + p2<br>

**思路**：<br>
如果不考虑走多少步，只计算有多少种方法时：要想走到p位置，前一位置是p-1, 或者p-2,所以<br>
到达p位置的方法数是两者之和，p-2位置只能考虑步进2，因为步进1就成了p-1


```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p1, p2 = 2, 1
        for i in range(4, n+1):
            p1, p2 = p1 + p2, p1
        return p1 + p2
```


```python

```

**题目2**：最小路径和-64题<br>
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。<br>

说明：每次只能向下或者向右移动一步。<br>

**示例**:<br>

输入:<br>
[<br>
  [1,3,1],<br>
  [1,5,1],<br>
  [4,2,1]<br>
]<br>
输出: 7<br>
解释: 因为路径 1→3→1→1→1 的总和最小。<br>

**思路**：到达每一个pos的路径分为从左和从上，采用的动规的思想先计算第一行的值备份，<br>
    然后利用状态转移共识推进<br>
**状态转移**：pij = lst[i][j] + min(pi,j-1   pi-1,j)


```python
class Solution:
    def minPathSum(self, grid):        
        X, Y = len(grid[0]), len(grid)
        for i in range(1, X):
            grid[0][i] = grid[0][i] + grid[0][i-1]       

        for j in range(1, Y):
            grid[j][0] = grid[j][0] + grid[j-1][0]       
        
        for i in range(1, X):
            for j in range(1, Y):
                grid[j][i] = grid[j][i] + min(grid[j][i-1], grid[j-1][i])
        return grid[-1][-1]
       

```

思路2： 维护一维数组而不是二维数组降低空间复杂度


```python
class Solution:
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])  # 行 列
        dp = [0] * c
        for i in range(r):
            for j in range(c):
                if j == 0:  # 第0列，数据直接继承上面的结果，最后要加上自己
                    dp[j] = dp[j]
                elif i == 0:  # 第0行
                    dp[j] = dp[j - 1]
                else:
                    dp[j] = min(dp[j - 1], dp[j])
                dp[j] += grid[i][j]
        return dp[c - 1]
```


```python
    
```

**题目3**<br>
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。<br>

**示例**：<br>
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()<br>

sumRange(0, 2) -> 1<br>
sumRange(2, 5) -> -1<br>
sumRange(0, 5) -> -3<br>

**说明:**<br>
你可以假设数组不可变。<br>
会多次调用 sumRange 方法。<br>

来源：力扣303（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable

**思路**：<br>
但是仔细读题可以发现，是有问题的， 说明中提到“会多次调用 sumRange 方法”， 也就是说，对<br>
于一个数组来说，如果求解[2, 4]的累加，又求了[2,5]的累加，这样等于[2,4]的累加被重复计算了一<br>
遍，这就是问题的关键，也是动态规划和递归中常常要解决的，重复子问题。所以每次都逐个相加<br>
计算子区间的和不是理想的做法。<br>
**状态转移**<br>
p[i, j] = p[j+1] - p[i]


```python
class NumArray:
    def __init__(self, nums):
        self.nums = [0] + nums 
        pre = 0
        for i in range(1,len(self.nums)):
            pre += self.nums[i]
            self.nums[i] = pre        

    def sumRange(self, i, j):      
        return self.nums[j+1] - self.nums[i]   
```


```python

```

**题目4-整数分割**<br>
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。<br>

**示例 1**:<br>
输入: 10<br>
输出: 36<br>
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。<br>
说明: 你可以假设 n 不小于 2 且不大于 58。<br>

来源：力扣343（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break<br>


```python
class Solution:
    def integerBreak(self, n):
        res = [0, 1]  # 开头         
        for i in range(2, n+1):
            tmp = 0
            for j in range(1, i):
                # 第一个是记忆值，后两个是新的计算值，区别在于对j是否拆分
                tmp = max(tmp, (i-j) * res[j], (i-j)*j)  
            res.append(tmp)
        return res[n]
```


```python

```

**题目5-最长上升子序列**<br>
给定一个无序的整数数组，找到其中最长上升子序列的长度。<br>

**示例:**<br>

输入: [10,9,2,5,3,7,101,18]<br>
输出: 4 <br>
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。<br>

说明:<br>
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。<br>
你算法的时间复杂度应该为 O(n2) 。<br>
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?<br>
<br>
来源：力扣300（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence<br>

**思路**<br>
dp：由左向右推进，计算到当前位置的最长子序列<br>
状态转移：设i为上层，j为子层，在确定位置i的最长子序列长度时：<br>
如果**nums[j] < nums[i]** : dp[i] = dp[j]+1,如果一个序列以nums[j]结尾，对应的最长子序列长度为dp[j]那么加上dp[i]后长度加1<br>
如果**nums[j] >= nums[i]** 对长度没有影响，跳过。<br>
通俗理解，循环遍历，**降维打击**。<br>


```python
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:return 0
        dp=[1]*len(nums)  # 初始化
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```


```python
a = Solution()
a.lengthOfLIS([10,9,2,5,3,7,101,18])
```




    4




```python

```

**题目6-分割等和子集**<br>
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成**两个子集**，使得两个子集的元素和相等。<br>

**注意**:<br>
每个数组中的元素不会超过 100<br>
数组的大小不会超过 200<br>

**示例**:<br>
输入: [1, 2, 3, 5]
输出: false

解释: 数组不能分割成两个元素和相等的子集.<br>

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum

知识点：背包问题，现在考虑用动规解决<br>
目标值：sum(nums)*0.5，外层为nums列表，子层为目标值到当前值是否可以由列表中的值加和求得<br>


```python
class Solution:
    def canPartition(self, nums):
        if sum(nums)%2 != 0:
            return False
        dst = sum(nums) // 2
        
        dp = [False] * (1+dst)
        dp[0] = True
        for num in nums:
            for i in range(dst, num-1, -1):
                dp[i] = dp[i] or dp[i-num]  # 保证出现自身时，相应的位置为True
        return dp[-1] 
```


```python

```

**题目7-股票交易**<br>
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​<br>

设计一个算法计算出**最大利润**。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:<br>

你不能同时参与多笔交易（**你必须在再次购买前出售掉之前的股票**）。<br>
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。<br>
示例:<br>

输入: [1,2,3,0,2]<br>
输出: 3 <br>
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]<br>

来源：力扣309（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown



```python

```

**题目8-公共子序列**<br>
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。<br> 

**示例**：<br>

输入: "sea", "eat"<br>
输出: 2<br>
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"<br>
 

**提示**：<br>

给定单词的长度不超过500。<br>
给定单词中的字符只含有小写字母。<br>

来源：力扣583（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings<br>

**思路**：<br>
解决LCS问题，需要把原问题分解成若干个子问题，所以需要刻画LCS的特征。<br>

设A=“a0，a1，…，am”，B=“b0，b1，…，bn”，且Z=“z0，z1，…，zk”**为它们的最长公共子序列**。不难证明有以下性质：<br>
性质1：<font color=#FF0000>**同余必公**:</font>，如果am=bn，则zk=am=bn，且“z0，z1，…，z(k-1)”是“a0，a1，…，a(m-1)”和“b0，b1，…，b(n-1)”的一个最长公共子序列；<br>
性质2：<font color=#FF0000>**异类可删**:</font>，如果am!=bn，则若zk!=am，蕴涵“z0，z1，…，zk”是“a0，a1，…，a(m-1)”和“b0，b1，…，bn”的一个最长公共子序列；<br>
如果am!=bn，则若zk!=bn，蕴涵“z0，z1，…，zk”是“a0，a1，…，am”和“b0，b1，…，b(n-1)”的一个最长公共子序列。<br>
用**反证法**可以证明

**状态转移**<br>
用X表示str1， Y表示str2&nbsp;&nbsp;&nbsp;&nbsp;
xi表示[x1，x2，...xi]&nbsp;&nbsp;&nbsp;
yj表示[y1，y2，...yj]<br>
运用以上两个性质有：<br>
<font color=#FF0000>**c[ij]=c[i-1, j-1]+1**</font>;&nbsp;if&nbsp;xi&nbsp;=&nbsp;yj<br>
<font color=#FF0000>**c[ij]=max{c[i-1, j],c[i, j-1]};**</font>&nbsp;if&nbsp;xi&nbsp;!=&nbsp;yj<br>


```python
class Solution: 
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]  # 注意不可以改变nm的位置，和循环体、返回值索引对应
        for i in range(1, m+1):  # dp表中维护的最长索引是m和单词1长度保持一致
            for j in range(1, n+1):  # dp表中维护的最长索引是n和单词2长度保持一致
                if word1[i-1] == word2[j-1]:  # python索引从0开始
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
      
        return m + n - 2 * dp[m][n]

```


```python
a = Solution()
a.minDistance('', 'b')
```




    1




```python
len('')
```




    0




```python

```
