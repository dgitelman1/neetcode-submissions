class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cur, prev = [0]*(len(t)+1), [0]*(len(t)+1)
        cur[-1] = 1
        prev[-1] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i]==t[j]:
                    cur[j] = prev[j] + prev[j+1]
                else:
                    cur[j] = prev[j]
            cur, prev = prev, cur
        return prev[0]