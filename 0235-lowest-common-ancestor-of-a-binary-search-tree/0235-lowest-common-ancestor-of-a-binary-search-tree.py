# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, r: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        mi=min(p.val,q.val)
        ma=max(p.val,q.val)
        while r!=None:
            if(mi<r.val and ma<r.val):
                r=r.left
            elif(mi>r.val and ma>r.val):
                r=r.right
            else:
                break
        return r