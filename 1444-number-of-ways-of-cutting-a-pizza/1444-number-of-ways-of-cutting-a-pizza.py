class Solution:
    def ways(self, p: List[str], k: int) -> int:
        m, n = len(p), len(p[0])
        a = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                c=0;
                if(p[i][j]=='A'):
                    c=1;
                a[i][j]=a[i+1][j]+a[i][j+1]-a[i+1][j+1]+c
        m={}            
        print(a)
        
        def tra(r,c,k):
            s=(r,c,k)
            if s in m:
                return m[s]
            if a[r][c]==0:
                return 0
            if k==0:
                return 1
            ans=0;
            for i in range(r+1,len(a)):
                if (a[r][c]-a[i][c])>0 :
                    ans+=tra(i,c,k-1)
                    ans%=1000000007
                    
            for j in range(c+1,len(a[0])):
                if (a[r][c]-a[r][j])>0 :
                    ans+=tra(r,j,k-1)
                    ans%=1000000007
            
            m[s]=ans
            return ans%1000000007
        
        return tra(0,0,k-1)