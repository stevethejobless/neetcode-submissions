class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = ['{', '[', '(']
        close2open = {'}' : '{', ']' : '[', ')' : '(' }
        stack = []
        for i in range( len(s)):
            if s[i] in openbrackets :
                stack.append(s[i])
            elif len(stack) > 0 and close2open[s[i]] == stack.pop():
                pass
            else: return False
        if len(stack) == 0: return True
        else: return False