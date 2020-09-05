class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            return gcd(b, a % b) if b else a
        def check(mid):
            res = mid // a + mid // b + mid // c - mid // x - mid // y - mid // z + mid // t
            return n <= res
        # math.gcd
        x = a * b / gcd(a, b)
        y = b * c / gcd(b, c)
        z = a * c / gcd(a, c)
        t = x * c / gcd(x, c)
        # 二分法模板
        l = min(a, b, c)
        r = l * n + 1
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l - min(l % a, l % b, l % c)
