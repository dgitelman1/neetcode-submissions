class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[0]*(n+1)]*(m+1)
        num_paths[1][1]=1
        for i in range(1, m+1):
            for j in range(1, n+1):
                num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]
        return num_paths[-1][-1]
