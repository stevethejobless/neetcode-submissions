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
        stack = deque([node])
        copied = {}
        while stack:
            cur = stack.popleft()
            if cur not in copied:
                copied[cur] = Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor not in copied:
                    copied[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                copied[cur].neighbors.append(copied[neighbor])
        return copied[node]
                


        