class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for p in s:
            if p in mapping:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top!=mapping[p]:
                    return False
            else:
                stack.append(p)
        return len(stack)==0