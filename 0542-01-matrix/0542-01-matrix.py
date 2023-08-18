class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        
        dp=[[10000]*(len(m[0])) for _ in range(len(m))]
        for  i in range(0,len(m)):
            for j in range(0,len(m[0])):
                if m[i][j]==1:
                    t= dp[i-1][j] if i>0 else 10000
                    d= dp[i][j-1] if j>0 else 10000
                    dp[i][j]=min(t,d)+1
                    
                else:
                    dp[i][j]=0
        #print(dp)
        for  i in range(len(m)-1,-1,-1):
            for j in range(len(m[0])-1,-1,-1):
                if m[i][j]==1:
                    t= dp[i+1][j] if i<len(m)-1 else 10000
                    d= dp[i][j+1] if j<len(m[0])-1 else 10000
                    dp[i][j]=min(t+1,d+1,dp[i][j])
                else:
                    dp[i][j]=0
        return dp