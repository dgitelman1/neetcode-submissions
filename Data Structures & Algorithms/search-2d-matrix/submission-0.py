class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS*COLS
        while l<r:
            m = (l+r-1)//2
            cur = matrix[m//COLS][m%COLS]
            if cur==target:
                return True
            if cur<target:
                l = m+1
            else:
                r=m
        return False