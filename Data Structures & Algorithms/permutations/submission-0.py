class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for each nums, we can either have it be the first item in the current permutation or not
        # for each i, either keep it as current start or don't 
        output = []
        def dfs(cur, cur_nums):
            # base case
            if len(cur)==len(nums):
                output.append(cur.copy())
            # we can break into sub permutations - at each point, we want to find permutations that are left and append them to what we have
            # this means that for each potential point, we want to go through the potential starting positions, and append it to the cur, and then pass cur_nums as the array without that point
            for i in range(len(cur_nums)):
                cur.append(cur_nums[i])
                dfs(cur, cur_nums[0:i]+cur_nums[i+1:len(cur_nums)])
                cur.pop()
        dfs([], nums)
        return output
            
