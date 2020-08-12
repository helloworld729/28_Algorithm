class Solution:
    def strToInt(self, sstr: str) -> int:
        def atoi(s):
            ll = len(s)
            res, weight = 0, 0
            for i in range(ll-1, -1, -1):
                res += int(s[i]) * pow(10, weight)
                weight += 1
            return res

        # 处理正负号
        sstr = sstr.strip()
        if not sstr or sstr[0].isalpha():return 0
        neg = 1
        if sstr[0] == "-" or sstr[0] == "+":
            sstr = sstr[1:]
            neg = -1 if sstr[0] == "-" else 1

        # 处理字母
        cut = ll = len(sstr)
        for i in range(ll):
            if not sstr[i].isdigit():
                cut = i  # watch
                break

        if cut >= 1:  # watch
            res = neg * atoi(sstr[:cut])
            if res < 0:
                return max(res, -2147483648)
            return min(res, pow(2, 31)-1)
        else: return 0

a = Solution()
s = "3.14159"
print(a.strToInt(s))