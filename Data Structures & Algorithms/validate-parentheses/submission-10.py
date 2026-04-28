class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = ['{', '[', '(']
        close2open = {'}' : '{', ']' : '[', ')' : '(' }
        stack = []
        for c in s:
            if c in openbrackets :
                stack.append(c)
            elif stack and close2open[c] == stack.pop():
                pass
            else: return False
        else: return True if not stack else False