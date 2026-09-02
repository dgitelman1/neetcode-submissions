class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        found = set()
        def dfs(i, current_sum):
            if current_sum==target and tuple(subset) not in found:
                output.append(subset.copy())
                found.add(tuple(subset))
                return
            if i>=len(nums) or current_sum>=target:
                return
            subset.append(nums[i])
            dfs(i, current_sum+nums[i])
            dfs(i+1, current_sum+nums[i])
            subset.pop()
            dfs(i+1,current_sum)
        dfs(0,0)
        return output