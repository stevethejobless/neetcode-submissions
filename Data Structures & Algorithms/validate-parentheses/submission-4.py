class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        s_lst = list(s)
        while i< len(s_lst)-1:
            if s_lst[i] == '(' and s_lst[i+1] == ')':
                del s_lst[i]
                del s_lst[i]
                i=0
            elif s_lst[i] == '[' and s_lst[i+1] == ']':
                del s_lst[i]
                del s_lst[i]
                i=0
            elif s_lst[i] == '{' and s_lst[i+1] == '}':
                del s_lst[i]
                del s_lst[i]
                i=0
            else: i+=1
        if len(s_lst) == 0: return True
        else: return False
