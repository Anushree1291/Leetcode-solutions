class Solution:
    def maxValue(self, e: List[List[int]], k: int) -> int:
        e.sort()
        dp=[[-1]*(len(e)) for _ in range(k+1)]
        starts=[i for i,j,k in e]
        
        def tra(ind,co):
            if co==0 or ind==len(e):
                return 0
            if dp[co][ind]!=-1:
                return dp[co][ind]
            
            nind=bisect_right(starts,e[ind][1])
            dp[co][ind]=max(tra(ind+1,co),e[ind][2]+tra(nind,co-1))
            
            return dp[co][ind]
        
        return tra(0,k)