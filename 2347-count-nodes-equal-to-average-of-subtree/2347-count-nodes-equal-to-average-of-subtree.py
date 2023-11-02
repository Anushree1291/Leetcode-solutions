# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.c=0

        def tra(r):
            if not r:
                return [0,0]
            
            a=tra(r.left)
            b=tra(r.right)
            s=a[0]+b[0]+r.val
            n=a[1]+b[1]+1

            if s//n == r.val:
                self.c+=1
            
            return [s,n]

        d=tra(root)
        return self.c