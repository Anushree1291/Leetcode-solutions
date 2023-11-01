# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        m=defaultdict(int)
        
        def tra(r):
            if not r:
                return
            m[r.val]+=1
            tra(r.left)
            tra(r.right)
            return

        
        tra(root)
        ma=max(m.values())
        ans=[]
        for i in m:
            if m[i]==ma:
                ans.append(i)
        return ans