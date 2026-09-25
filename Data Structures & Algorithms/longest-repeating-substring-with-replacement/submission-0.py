class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find the longest substring with 
        # k + max_freq = string size
        # k <= string size - maxfreq
        # keep track of max frequency of char
        # array of 26 - increase
        # we can either increase the window size, if max freq also goes up or we cna increase string size
        # if k = string_size - maxfreq we increment left and update freqsxs
        freqs = [0]*26
        max_freq = 0
        l, r = 0, 0
        while r<len(s):
            freqs[ord(s[r])-ord('A')]+=1
            max_freq = max(max_freq, freqs[ord(s[r])-ord('A')])
            if k < (r-l+1)-max_freq:
                freqs[ord(s[l])-ord('A')]-=1
                l+=1
            r+=1
        return r-l