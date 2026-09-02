class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = [0]*(n+2)
        total_ways[1] = 1
        for i in range(2, n+2):
            print(total_ways)
            print(i)
            total_ways[i] = total_ways[i-1]+total_ways[i-2]
        return total_ways[-1]