# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        
        def tra(node):
            a=None
            if(node ==None):
                return None
            if(node.val==v):
                return node
            a=tra(node.left)
            if(a!=None):
                return a;
            a=tra(node.right)
            if(a!=None):
                return a;
            return a
        
        return tra(root)