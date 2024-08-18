class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a=[0]*(n+1)
        a[0]=1
        x,y,z=0,0,0
        for i in range(1,n+1):
            a[i]=min(a[x]*2,a[y]*3,a[z]*5)
            if a[i]==a[x]*2:
                x+=1
            if a[i]==a[y]*3:
                y+=1
            if a[i]==a[z]*5:
                z+=1
        return a[n-1]