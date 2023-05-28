class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        m={}
        
        def tra(i,j):
            if (i,j) in m:
                return m[i,j]
            
            res=10000000
            a=0
            c=0
            for x in range(len(cuts)):
                k=cuts[x]
                if(k>i and k<j ):
                    a=tra(i,k)+tra(k,j)+(j-i)
                    c+=1
                    res=min(res,a)
            if(c==0):
                m[i,j]=0
            else:
                m[i,j]=res
            return m[i,j]
        
        return tra(0,n)