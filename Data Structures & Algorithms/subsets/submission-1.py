class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number we have subsets that include that number and subsets that don't
        output = [[]]
        res = []
        def helper(i):
            # at i we can either include or disclude the current i
            # then we can move onto the next i for each group
            if i>=len(nums):
                return
            res.append(nums[i])
            output.append(res.copy())
            helper(i+1)
            res.pop()
            helper(i+1)
        helper(0)
        return output