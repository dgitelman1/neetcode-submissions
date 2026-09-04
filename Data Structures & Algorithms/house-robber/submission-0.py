class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        no_rob = 0
        # each point we can either rob or not rob, and only care about whether the last house was robbed or not
        # if we rob, then the most we can make at that point is the amt given we didn't rob the last house + the amt we make
        # we if we don't rob, then the most we can make at that point is the max between robbing the last house and if we didnt rob the last house
        for i in range(0, len(nums)):
            no_rob, rob = max(no_rob, rob), no_rob+nums[i]
        return max(no_rob, rob)