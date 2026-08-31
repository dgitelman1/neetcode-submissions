class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can maintain a set of seen characters, and two pointers
        # if we see a duplicate character we can increase the left pointer until it's gone
        # why does this work? eventually, if we keep increasing a sliding window, we will see the longest string with duplicate characters, since this must be a contigous substring
        seen = set()
        l, r = 0, 0
        max_seen = 0
        while r < len(s):
            current_char = s[r]
            while current_char in seen:
                seen.remove(s[l])
                l+=1
            seen.add(current_char)
            max_seen = max(len(seen), max_seen)
            r+=1
        return max_seen