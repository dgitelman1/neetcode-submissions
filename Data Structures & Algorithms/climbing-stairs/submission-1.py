class Solution:
    def climbStairs(self, n: int) -> int:
        # we only really care about two steps before and one step before counts
        one_before = 1
        two_before = 0
        current = 0
        for i in range(1, n+1):
            current = one_before + two_before
            two_before = one_before
            one_before = current

        return current