class Solution:
    def getRow(self, r: int) -> List[int]:
        ans=[None]
        for i in range (r+1):
            a=[1]*(i+1)
            m=(i>>1)+1
            for j in range(1,m):
                v=ans[j-1]+ans[j]
                a[j],a[len(a)-j-1]=v,v
            ans=a
        return ans