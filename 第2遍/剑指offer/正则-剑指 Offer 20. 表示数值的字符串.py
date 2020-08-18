# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/submissions/
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        pattern = "[+-]?\d+(\\.\d+)?[eE]?\d+|\d?\\.\d*|\d+"
        res = re.match(pattern, s)
        # print(res.end(), len(s))
        if res and res.end() == len(s): return True
        return False

a = Solution()
print(a.isNumber("0e"))