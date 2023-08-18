from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        a=[0]*n
        for (i,j) in roads:
            a[i]+=1
            a[j]+=1
        
        m=0
        for i in range(n):
            for j in range(i+1,n):
                c=a[i]+a[j]
                if [i,j] in roads or [j,i] in roads:
                    c-=1
                    #print(i,j)
                m=max(m,c)
        return m