class Solution:
    def findTargetSumWays(self, n: List[int], t: int) -> int:
        dp={}

        def tra(i,s):
            if i==len(n):
                return 1 if s==t else 0
            
            if (i,s) in dp:
                return dp[(i,s)]
            
            dp[(i,s)]=tra(i+1,s+n[i]) + tra(i+1,s-n[i])
            return dp[(i,s)]
        
        tra(0,0)
        return dp[(0,0)]