# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l=[]
        q=[]
        q.append(root)
        while q:
            a=len(q)
            p=[]
            while a!=0:
                a-=1
                i=q.pop(0)
                p.append(i.val)
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
            l.insert(0,p)
        return l
                