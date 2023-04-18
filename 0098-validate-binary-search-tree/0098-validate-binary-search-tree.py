# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = sys.maxsize
        
        def tra(l,u,r):
            if not r:
                return True
            elif r.val>=u or r.val<=l:
                return False 
            else:
                return tra(l,r.val,r.left) and tra(r.val,u,r.right)
            
        return tra(-INF,INF,root)
        