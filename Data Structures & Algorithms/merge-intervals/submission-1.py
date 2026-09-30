class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        output.append(intervals[0])
        curEnd = intervals[0][1]
        # for each interval, if the start is before the current end, we know that we will need to merge them together. We can keep the cur end, and then update the latest point in the output if we have an intersection between it and the current point. Otherwise, we can jsut append the interval to the output
        for start, end in intervals[1:]:
            if curEnd>=start:
                output[-1][1] = max(end, curEnd)
            else:
                output.append([start, end])
            curEnd = max(end, curEnd)
        return output