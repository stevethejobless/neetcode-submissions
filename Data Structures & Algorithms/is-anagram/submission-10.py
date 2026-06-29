class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            print(len(s),len(t))
            return False
        
        s_map = {}
        t_map = {}
        for i in s:
            if i in s_map:
                s_map[i] = s_map[i] + 1
            else:
                s_map[i] = 1
        for i in t:
            if i in t_map:
                t_map[i] = t_map[i] + 1
            else:
                t_map[i] = 1
        print(s_map)
        print(t_map)
        for key in s_map:
            if key in t_map and s_map[key] == t_map[key]:
                continue
            else:
                return False
        return True