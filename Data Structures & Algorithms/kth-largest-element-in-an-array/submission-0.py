class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_max = [-n for n in nums]
        heapq.heapify(nums_max)
        for _ in range(0, k-1):
            heapq.heappop(nums_max)
        return -heapq.heappop(nums_max)