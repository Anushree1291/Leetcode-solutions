class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p=sorted(p)
        ans=0
        j=0
        for i in range(len(p)-1,-1,-1):
            if(j>i):
                break
            ans+=1
            if(p[i]+p[j]<=l):
                j+=1
        return ans