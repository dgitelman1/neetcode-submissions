class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(cur_n, cur_str, left):
            if cur_n==0:
                output.append(cur_str)
                return
            # if we have enough valid parens left, we can always append a left
            if cur_n-left>0:
                backtrack(cur_n, cur_str+'(', left+1)
            if left>0:
                backtrack(cur_n-1, cur_str+')', left-1)
        backtrack(n, '', 0)
        return output