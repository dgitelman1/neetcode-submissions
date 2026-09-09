class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # at each point, we can either continue adding the current number, or not add anymore, so we should iterate to a new number to add
        output = []
        def backtrack(i, cur):
            if i>=len(nums):
                output.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            j = i
            while j<len(nums) and nums[i]==nums[j]:
                j+=1
            backtrack(j, cur)
        backtrack(0, [])
        return output