class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[None]*n
        for i in range(n):
            r,m= [1]*(i+1) , (i>>1)+1
            for j in range(1,m):
                v=ans[i-1][j-1]+ans[i-1][j]
                r[j],r[len(r)-j-1]=v,v
            ans[i]=r
        return ans