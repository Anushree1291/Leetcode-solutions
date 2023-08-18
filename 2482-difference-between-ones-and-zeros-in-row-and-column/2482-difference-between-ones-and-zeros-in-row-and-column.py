from typing import List
class Solution:
    def onesMinusZeros(self, g: List[List[int]]) -> List[List[int]]:
        m=len(g)
        n=len(g[0])
        r=[0]*m
        c=[0]*(n)
        for i in range(m):
            for j in range(n):
                if g[i][j]==1:
                    r[i]+=1
                    c[j]+=1
        
        for i in range(m):
            for j in range(n):
                g[i][j]=(r[i]+c[j])*2-m-n
        
        return g