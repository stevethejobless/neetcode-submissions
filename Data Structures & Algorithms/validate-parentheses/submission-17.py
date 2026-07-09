class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',']':'[',')':'('}
        stack = [] #Os(n)
        for char in s: #Ot(n)
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0