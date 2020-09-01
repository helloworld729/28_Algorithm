class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def div(dividend, divisor):
            if dividend < divisor: return 0
            if divisor == 1: return dividend
            ans = 1
            back = divisor
            while dividend >= divisor:
                divisor <<= 1
                if dividend >= divisor:
                    ans <<= 1
            divisor >>= 1
            return ans + self.divide(dividend - divisor, back)

        flag1 = 1 if divisor > 0 else -1
        flag2 = 1 if dividend > 0 else -1
        flag = flag1 * flag2

        ret = div(abs(dividend), abs(divisor)) * flag
        if ret > 0:
            return min(ret, pow(2,31)-1)
        else:
            return max(ret, -1*pow(2, 31))

"""
思路：设定最小商，被除数增加1倍，商增加1倍直到除数大于被除数
用余项递归计算。
"""