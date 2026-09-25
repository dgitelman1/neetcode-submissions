class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0]*len(temperatures)
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            while stack and stack[-1][0] < cur_temp:
                _, j = stack.pop()
                results[j] = i-j
            stack.append((cur_temp, i))
        return results