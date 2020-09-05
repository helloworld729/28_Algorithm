class Solution:
    def permutation(self, s: str):
        result = []

        def advance(have, cans):
            ll = len(cans)
            if not ll:
                result.append("".join(have))
                return
            back = {}
            for i in range(ll):
                if back.get(cans[i], 0):
                    continue
                back[cans[i]] = 1
                have.append(cans[i])
                advance(have, cans[:i] + cans[1 + i:])
                have.pop()

        advance([], s)
        return result
