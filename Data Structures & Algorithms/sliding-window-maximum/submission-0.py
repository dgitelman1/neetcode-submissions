class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if we move the sliding window and the val we move it to is the new max we know that all the previous vals in the window will never be the real max so we can get rid of them
        # otherwise it might be the max if the biggest one is popped
        queue = deque()
        r = 0
        output = []
        while k>0:
            while queue and queue[-1]<nums[r]:
                queue.pop()
            queue.append(nums[r])
            r+=1
            k-=1
        l=0
        while r<len(nums):
            output.append(queue[0])
            if queue[0]==nums[l]:
                queue.popleft()
            l+=1
            while queue and queue[-1]<nums[r]:
                queue.pop()
            queue.append(nums[r])
            r+=1
        output.append(queue[0])
        return output