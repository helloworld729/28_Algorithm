class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll = len(s)
        if not ll: return 0
        l = 0
        r = cur = 1
        hashmap = {s[0]: 0}
        max_len = 1

        while r <= ll - 1:
            cans = s[r]  # 当前值
            # 不在当前的窗口
            if cans not in hashmap or hashmap[cans] < l:
                cur += 1
                hashmap[cans] = r
            else:
                cur -= (hashmap[cans] - l + 1)  # 历史长度
                cur += 1                        # 新增一位
                l = hashmap[cans] + 1           # 左边界推进
                hashmap[cans] = r               # 字典更新
            r += 1
            max_len = max(max_len, cur)

        return max_len

# 时间复杂度：O(N)
# 空间复杂度：O(N)

