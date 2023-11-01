class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        m=len(o)
        n=len(o[0])
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1 and o[i-1][j-1]!=1:
                    continue
                else:
                    if o[i-1][j-1]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        #print(dp)
        return dp[m][n]