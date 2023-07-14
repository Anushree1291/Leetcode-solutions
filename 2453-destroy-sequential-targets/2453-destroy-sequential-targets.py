class Solution:
    def destroyTargets(self, n: List[int], s: int) -> int:
        dp={}
        res=0
        ind=0
        n.sort()
        for i in range(len(n)-1,-1,-1):
            nu=n[i]%s
            prev=dp.get(nu,0)
            dp[nu]=prev+1
            if(dp[nu]>=res):
                res=dp[nu]
                ind=n[i]
        #print(dp)
        return ind