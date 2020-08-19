class Solution:
    def permutation(self, s: str):
        res = []
        ll = len(s)
        if ll <= 1: return [s]
        visited = {}
        for i in range(ll):
            if not visited.get(s[i], False):
                for d in self.permutation(s[:i] + s[i+1:]):
                    res.append(s[i]+d)
                visited[s[i]] = True
        return res

