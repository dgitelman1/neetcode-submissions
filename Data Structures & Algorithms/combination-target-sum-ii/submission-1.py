class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def dfs(i, cur, total):
            if total==target:
                output.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            # at each point, we can either include or exclude the current point
            # if we include it, we want to iterate until we have a new i which is a new number
            # and run dfs from there
            # if we exclude it then we want to iterate until we have a new i which is a new number
            # iterate to next number - either keep or don't keep current i
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            j=i
            while j<len(candidates) and candidates[j]==candidates[i]:
                j+=1
            dfs(j, cur, total)
        dfs(0, [], 0)
        return output