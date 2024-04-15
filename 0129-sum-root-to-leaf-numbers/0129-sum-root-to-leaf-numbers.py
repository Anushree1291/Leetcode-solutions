# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, r: Optional[TreeNode]) -> int:
        self.s=0

        def tra(a,i):
            if not a.left and not a.right:
                self.s+=i*10+a.val
                return
            if a.left : tra(a.left,i*10+a.val)
            if a.right : tra(a.right,i*10+a.val)
            return
        
        tra(r,0)
        return self.s