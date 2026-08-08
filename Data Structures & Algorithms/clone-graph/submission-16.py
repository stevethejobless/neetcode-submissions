from collections import deque
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
        copied = {}
        copied[node] = Node(node.val)
        stack = deque([node])
        while stack:
            n = stack.popleft()
            cn = copied[n]
            for nei in n.neighbors:
                if nei not in copied:
                    copied[nei] = Node(nei.val)
                    stack.append(nei)
                cn.neighbors.append(copied[nei])
        return copied[node]


            
