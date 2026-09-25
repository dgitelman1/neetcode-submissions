class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we only care about state at current window
        # window len(s1) - we want to match character frequencies in s1 to s2
        if len(s1) > len(s2):
            return False
        s1_freqs = [0]*26
        for c in s1:
            s1_freqs[ord(c)-ord('a')]+=1
        s2_freqs = [0]*26
        l, r = 0, 0
        for _ in range(len(s1)):
            s2_freqs[ord(s2[r])-ord('a')]+=1
            r+=1
        while r<len(s2):
            if s1_freqs==s2_freqs:
                return True
            else:
                s2_freqs[ord(s2[l])-ord('a')]-=1
                l+=1
                s2_freqs[ord(s2[r])-ord('a')]+=1
                r+=1
        return s1_freqs == s2_freqs