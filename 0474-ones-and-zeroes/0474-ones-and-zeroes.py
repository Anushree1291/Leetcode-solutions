class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for st in s:
            z=st.count('0')
            o=len(st)-z
            
            for i in range(m,z-1,-1):
                for j in range(n,o-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-z][j-o]+1)
        
        return dp[m][n]