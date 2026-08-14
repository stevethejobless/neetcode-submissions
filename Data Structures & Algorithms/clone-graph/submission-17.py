"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copied = {}
        visit = set()
        def dfs(node):
            if node in visit:
                return
            if node not in copied:
                copied[node] = Node(node.val)
            if node.neighbors:
                for neighbor in node.neighbors:
                    if neighbor not in copied:
                        copied[neighbor] = Node(neighbor.val)
                        dfs(neighbor)
                    copied[node].neighbors.append(copied[neighbor])
            return copied[node]
        
        return dfs(node) if node else None
