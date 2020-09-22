class Solution:
    def findSwapValues(self, array1, array2):
        """最好O(N方)复杂度"""
        array1.sort()
        array2.sort()
        sum1, sum2 = sum(array1), sum(array2)
        diff = sum2 - sum1
        if diff & 1:  # 奇数
            return []
        target = diff // 2

        # 目标：从array2 中选一个数b， 从array1中选一个数a，是的b-a == target
        for b in array2:
            for a in array1:
                gap = b - a
                if gap == target:
                    return [a, b]
                elif gap < target:
                    break
        return []

    def findSwapValues2(self, array1, array2):
        """O(N)复杂度"""
        sum1, sum2 = sum(array1), sum(array2)
        diff = sum2 - sum1
        if diff & 1:  # 奇数
            return []
        target = diff // 2
        # 目标：从array2 中选一个数b， 从array1中选一个数a，是的b-a == target
        array1 = set(array1)
        for b in array2:
            if b - target in array1:
                return [b - target, b]
        return []

