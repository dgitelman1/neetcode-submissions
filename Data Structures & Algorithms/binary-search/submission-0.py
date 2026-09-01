class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while r>l:
            m = (l+r)//2
            cur_num = nums[m]
            if cur_num>target:
                r = m
            elif cur_num<target:
                l=m+1
            else:
                return m
        return -1