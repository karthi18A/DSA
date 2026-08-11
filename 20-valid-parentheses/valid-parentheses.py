class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '([{':
                stack.append(i)
            elif not stack or {')':'(','}':'{',']':'['}[i]!=stack.pop():
                return False
        return not stack