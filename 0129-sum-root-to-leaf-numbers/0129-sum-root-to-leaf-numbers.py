# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, r: Optional[TreeNode]) -> int:
        
        def tra(a,r)->int:
            b=0
            c=0
            if(r.left==None and r.right==None):
                return (a+r.val)
            p=a+r.val
            if r.left is not None:
                b=tra(p*10,r.left)
                #print(b)
            if r.right is not None:
                c=tra(p*10,r.right)
                #print(c)
            return (b+c)
        
        return tra(0,r)