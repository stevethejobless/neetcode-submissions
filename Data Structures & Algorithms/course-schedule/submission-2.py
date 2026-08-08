class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for crs, pre in prerequisites:
            if crs not in preMap:
                preMap[crs] = []
            if pre not in preMap:
                preMap[pre] = []
            preMap[crs].append(pre)
        
        def dfs(crs,visit):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei,visit): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs,pre in prerequisites:
            if not dfs(crs,set()): return False
        return True
