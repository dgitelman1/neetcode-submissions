"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we can keep visited as val, if val is in visited we don't need to go through it again
        if not node:
            return None
        queue = deque([node])
        old2new = {}
        old2new[node] = Node(node.val)
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old2new:
                    old2new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old2new[cur].neighbors.append(old2new[neighbor])
        return old2new[node]
        