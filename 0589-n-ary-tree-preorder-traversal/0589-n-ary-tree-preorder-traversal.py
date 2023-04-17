"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        a=[]
        
        def tra(root):
            if root==None:
                return
            a.append(root.val)
            for i in root.children:
                tra(i)
                
        tra(root)
        return a