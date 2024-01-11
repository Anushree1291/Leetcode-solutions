# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.a=[]
        
        def tra(r):
            if not r:
                return
            tra(r.left)
            self.a.append(r.val)
            tra(r.right)
            return
        
        tra(root)
        return self.a