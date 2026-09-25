class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 
        n, m = len(grid), len(grid[0])
        queue = deque()
        FRESH = 1
        ROTTEN = 2
        num_fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==ROTTEN:
                    queue.append((i, j))
                if grid[i][j]==FRESH:
                    num_fresh+=1
        minutes = 0
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        while queue and num_fresh>0:
            l = len(queue)
            minutes+=1
            for _ in range(l):
                i, j = queue.popleft()
                for x, y in directions:
                    i_new, j_new = i+x, j+y
                    if i_new>=0 and i_new<n and j_new>=0 and j_new<m and grid[i_new][j_new]==FRESH:
                        grid[i_new][j_new] = ROTTEN
                        num_fresh-=1
                        queue.append((i_new, j_new))
        return -1 if num_fresh>0 else minutes
