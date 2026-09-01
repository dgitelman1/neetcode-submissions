class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for p in s:
            if p in mapping:
                if not stack or stack.pop()!=mapping[p]:
                    return False
            else:
                stack.append(p)
        return len(stack)==0