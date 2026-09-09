class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_reach = 0
        for i in range(len(nums)):
            if cur_reach<i:
                return False
            cur_reach = max(nums[i]+i, cur_reach)
        return True