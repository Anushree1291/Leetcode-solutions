class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n=len(p)
        
        @lru_cache(None)
        def tra(i,j):
            if(i>j) : return 0
            pa=(j-i)%2
            if (pa==1):
                return max((p[i]+tra(i+1,j)), (p[j]+tra(i,j-1)))
            else:
                return min((-p[i]+tra(i+1,j)),( -p[j]+tra(i,j-1)))
        
        return tra(0,n-1)>0