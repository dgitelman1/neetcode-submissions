class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        def dfs(i, j, cur):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if matrix[i][j] <= cur:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            best = 1
            for x, y in directions:
                best = max(best, 1+dfs(i+x, j+y, matrix[i][j]))
            dp[i][j] = best
            return best
        best = 0
        for i in range(n):
            for j in range(m):
                best = max(best, dfs(i, j, -1))
        return best

