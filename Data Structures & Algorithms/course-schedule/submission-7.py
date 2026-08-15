class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for src, tar in prerequisites:
            adjList[src].append(tar)
        
        loop = set()  # nodes in current DFS path (detects cycles)
        completed = set()  # nodes fully explored and safe
        
        def dfs(node):
            if node in loop:
                return False  # cycle detected
            if node in completed:
                return True  # already confirmed safe
            
            loop.add(node)
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
            loop.remove(node)
            completed.add(node)  # mark as fully explored
            return True
        
        for course in range(numCourses):
            if course not in completed:
                if not dfs(course):
                    return False
        return True