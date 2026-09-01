class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k can at minimum be 1, and at most be the max in the array
        # choose some amount and then caclulate if we can eat it in h hours
        # if we can, then we can decrease k, if not, we can increase k

        l, r = 1, max(piles)
        while r>l:
            m = (l+r)//2
            cur_h = 0
            for p in piles:
                cur_h+=-(p//-m)
            if cur_h <= h:
                r = m
            elif cur_h > h:
                l = m +1
        return r