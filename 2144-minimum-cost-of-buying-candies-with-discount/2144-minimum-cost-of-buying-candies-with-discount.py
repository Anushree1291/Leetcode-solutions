class Solution:
    def minimumCost(self, c: List[int]) -> int:
        c.sort()
        i=len(c)-1
        res=0
        while i>=0:
            if i>1:
                res+=c[i]+c[i-1]
                i=i-3
            else:
                res+=c[i]
                i-=1
            
        return res