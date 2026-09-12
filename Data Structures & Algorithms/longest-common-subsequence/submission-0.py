class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # we have 2d list of text1 len x text2 len
        # each 1 dtermines the longest substring at those indices
        cur_row, prev_row = [0]*(len(text1)+1), [0]*(len(text1)+1)
        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text2[i]==text1[j]:
                    cur_row[j] = prev_row[j+1]+1
                else:
                    cur_row[j] = max(cur_row[j+1], prev_row[j])
            cur_row, prev_row = prev_row, cur_row
        return prev_row[0]