"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        a={}
        
        def tra(n):
            if n in a:
                return a[n]
            
            c=Node(n.val)
            a[n]=c
            for i in n.neighbors:
                c.neighbors.append(tra(i))
            return c
        
        return tra(node) if node else None