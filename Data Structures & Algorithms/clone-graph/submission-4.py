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
                graphHash[node.val] = {"node" : Node(val=node.val)}

            if node.neighbors is not None:
                for neighbor in node.neighbors:
                    if neighbor.val not in graphHash:
                        graphHash[neighbor.val] = {"node":Node(val=neighbor.val) }
                    graphHash[node.val]["node"].neighbors.append(graphHash[neighbor.val]["node"])
                    if neighbor not in visit:
                        dfs(neighbor,visit)
        dfs(node,set())
        print(graphHash)
        return graphHash[1]["node"]


        