"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graphHash = {}
        def dfs(node,visit):
            visit.add(node)
            if node.val not in graphHash:
                graphHash[node.val] = Node(val=node.val)
            if node.neighbors is not None:
                for neighbor in node.neighbors:
                    if neighbor.val not in graphHash:
                        graphHash[neighbor.val] = Node(val=neighbor.val)
                    graphHash[node.val].neighbors.append(graphHash[neighbor.val])
                    if neighbor not in visit:
                        dfs(neighbor,visit)
        dfs(node,set())
        return graphHash[1]
