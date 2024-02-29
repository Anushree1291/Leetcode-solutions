# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, r: Optional[TreeNode]) -> bool:
        if not r:
            return True
        q=deque([r])
        l=0
        while q:
            pre=None
            for i in range(len(q)):
                node=q.popleft()
                if ((l%2==1 and (node.val%2==1 or ((pre is not None) and node.val>=pre))) or (l%2==0 and (node.val%2==0 or ((pre is not None )and node.val<=pre)))):
                    return False
                
                pre=node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l+=1
        return True