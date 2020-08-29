"""
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:
输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

https://leetcode-cn.com/problems/palindrome-pairs/solution/hui-wen-dui-by-leetcode-solution/
"""
class Solution:
    def palindromePairs(self, words):

        indices = {word[::-1]: i for i, word in enumerate(words)}  # 翻转：序号字典

        def findWord(s: str, left: int, right: int) -> int:
            """当前字符片段是否在lst中"""
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            """字符串区间的回文判断"""
            len = right-left+1
            for i in range(len//2):
                if s[left+i] != s[right-i]:
                    return False
            return True

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                # 在右侧检查回文，返回左侧在字典的索引
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:  # 排除自己
                        ret.append([i, leftId])
                # 在右侧检查回文，返回左侧在字典的索引
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret

