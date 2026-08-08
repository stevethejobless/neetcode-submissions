"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new_map = {}
        def dfs(node):
            if node in old_new_map:
                return old_new_map[node]
            copyNode = Node(node.val)
            old_new_map[node] = copyNode
            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            return copyNode
        return dfs(node) if node else None