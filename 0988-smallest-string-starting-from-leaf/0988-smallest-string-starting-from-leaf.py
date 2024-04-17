# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, ro: Optional[TreeNode]) -> str:
        self.st="zzzzzzzzzzzzzzz"
        def tra(r,s):
            if r.left is None and r.right is None:
                s=chr(r.val+97)+s
                if s<self.st:
                    self.st=s
                return
            if not r.left:
                tra(r.right,chr(r.val+97)+s)
            elif not r.right:
                tra(r.left,chr(r.val+97)+s)
            else:
                tra(r.right,chr(r.val+97)+s)
                tra(r.left,chr(r.val+97)+s)
            return

        tra(ro,"")
        return self.st