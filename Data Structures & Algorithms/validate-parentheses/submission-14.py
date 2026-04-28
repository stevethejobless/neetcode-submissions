class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {'}':'{', ')':'(', ']':'['}
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
            elif stack and stack[-1] == close2open[char]:
                stack.pop()
            else: 
                return False
        return True if not stack else False