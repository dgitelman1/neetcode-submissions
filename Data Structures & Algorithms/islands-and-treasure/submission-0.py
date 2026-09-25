class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def check_cell(i, j, dist):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==-1 or grid[i][j]<=dist:
                return False
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, dist = queue.popleft()
            for x, y in directions:
                if check_cell(i+x, j+y, dist+1):
                    grid[i+x][j+y] = dist+1
                    queue.append((i+x, j+y, dist+1))