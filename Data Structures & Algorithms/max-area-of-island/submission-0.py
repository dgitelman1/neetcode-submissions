class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        def bfs(i, j):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if grid[i][j]==0:
                return 0
            grid[i][j]=0
            total_area = 0
            for x, y in directions:
                total_area+=bfs(i+x, j+y)
            return 1 + total_area
        best = 0
        for i in range(n):
            for j in range(m):
                best = max(best, bfs(i,j))
        return best