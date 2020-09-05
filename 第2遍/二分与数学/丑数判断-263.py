# 判断一个数是不是和丑数
class Solution:
    def isUgly(self, num: int) -> bool:
        if not num: return False
        while True:
            if num % 2 == 0: num //= 2
            elif num % 3 == 0: num //= 3
            elif num % 5 == 0: num //= 5
            else: break
        return num == 1

