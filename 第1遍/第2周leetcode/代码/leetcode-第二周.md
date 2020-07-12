## 一、二分法

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx



```python
def sqrt(x):
    if x<=1:
        return x
    l, r = 0, x
    while l < r:
        mid = int(0.5 * ( l + r ))
        if mid * mid <= x:
            l = mid
        else:
            r = mid
        if (l + 1)==r:
            return l
    
```


```python
for i in range(5):
    print(i, sqrt(i), end=' ## ')
```

    0 0 ## 1 1 ## 2 1 ## 3 1 ## 4 2 ## 

## 二、分治

给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以<br>求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。<br>

示例 1:<br>
输入: "2\*3-4\*5"<br>
输出: [-34, -14, -10, -10, 10]<br>
解释: 
(2\*(3-(4\*5))) = -34 <br>
((2\*3)-(4\*5)) = -14 <br>
((2\*(3-4))\*5) = -10 <br>
(2\*((3-4)\*5)) = -10 <br>
(((2\*3)-4)\*5) = 10<br>

来源：力扣（LeetCode）241题目<br>
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses



```python
def diffcal(input: 'str'):
    return_list = []   
    for index, char in enumerate(input):
        if char in ['+', '-', '*']:  # 等式中可能有多个运算符
            left = diffcal(input[:index])
            right = diffcal(input[index+1:])
            
            for l in left:
                for r in right:
                    if char == '+':
                        return_list.append( l + r)
                    if char == '-':
                        return_list.append( l - r)
                    if char == '*':
                        return_list.append( l * r)
    if not return_list:  # 边界条件,兜底现场
        return_list.append(int(input))
    return return_list          
    
```


```python
diffcal("2*3-4*5")
```




    [-34, -10, -14, -10, 10]



基本运算器

实现一个基本的计算器来计算一个简单的字符串表达式的值。<br>

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。<br>

示例 1:<br>

输入: " 2-1 + 2 "<br>
输出: 3<br>

来源：力扣224（LeetCode）<br>
链接：https://leetcode-cn.com/problems/basic-calculator<br>


```python
def calculate(s: str) -> int:
    flag = True
    for index, char in enumerate(s):
        if char in ['+', '-']:
            flag = False
            left = calculate(s[:index])
            right = calculate(s[index+1:])
            
            if char == '+':
                answer = left + right
            elif char == '-':
                answer = left - right
    if flag:  # 边界条件
        answer = int(s)
    return answer     
    
```

## 三、哈希表-两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。<br>

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。<br>

示例:<br>

给定 nums = [2, 7, 11, 15], target = 9<br>

因为 nums[0] + nums[1] = 2 + 7 = 9<br>
所以返回 [0, 1]<br>

来源：力扣（LeetCode）<br>
链接：https://leetcode-cn.com/problems/two-sum<br>


```python
def twoSum(nums, target):
    infos = {}
    for index in range(len(nums)):
        if target - nums[index] in infos.keys():
            return [infos[target - nums[index]], index]        
        infos[nums[index]] = index
```


```python
twoSum([1,2,3,4], 5)
```




    [1, 2]



## 四、字符串-字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。<br>

示例 1:<br>

输入: s = "anagram", t = "nagaram"<br>
输出: true<br>
示例 2:<br>

输入: s = "rat", t = "car"<br>
输出: false<br>

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？<br>

来源：力扣242（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram


```python
def isAnagram(s: str, t: str) -> bool:
    infos = [0] * 26
    for char in s:
        infos[ord(char) - ord('a')] += 1  # ord返回acaii索引
    for char in t:
        infos[ord(char) - ord('a')] -= 1
    for i in infos:
        if i != 0:
            return False
    return True
```

测试：


```python
isAnagram( s = "rat", t = "car")
```




    False




```python
isAnagram(s = "anagram", t = "nagaram")
```




    True



  


```python
def isAnagram(s: str, t: str) -> bool:
    infos = {}
    for char in s:
        infos[char] = infos.get(char, 0) + 1  # get  方法查询键值，如果没有返回None，护着指定的默认值，此处为0
    for char in t:
        infos[char] = infos.get(char, 0) - 1
    for i in infos.values():
        if i != 0:
            return False
    return True
```

测试


```python
isAnagram('你好', '好啊')
```




    False




```python
isAnagram('你好', '你好')
```




    True



   


```python

```
