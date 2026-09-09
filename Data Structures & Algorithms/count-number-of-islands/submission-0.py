class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        def bfs(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            if grid[i][j]=='0':
                return False
            grid[i][j]='0'
            for x, y in directions:
                bfs(i+x, j+y)
            return True
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if bfs(i, j):
                    total+=1
        return total