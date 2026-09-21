class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] + [0] * (len(nums)-1)
        suffix = [0] * (len(nums)-1) + [nums[-1]]
        for i in range(1, len(nums)):
            prefix[i] = nums[i]*prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i]*suffix[i+1]
        output = [0]*len(nums)
        for i in range(1, len(nums)-1):
            output[i] = prefix[i-1]*suffix[i+1]
        output[0] = suffix[1]
        output[-1] = prefix[-2]
        return output