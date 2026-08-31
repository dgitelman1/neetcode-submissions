class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i in range(len(nums)):
            if target-nums[i] in remainders:
                return [remainders[target-nums[i]], i]
            remainders[nums[i]] = i
