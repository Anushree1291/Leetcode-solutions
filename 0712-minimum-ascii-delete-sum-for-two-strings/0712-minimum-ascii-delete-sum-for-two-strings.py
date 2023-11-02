class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp=[[-1 for _ in range(len(s2))] for _ in range(len(s1))]


        def tra(i,j):
            if i==len(s1) or j==len(s2):
                c=0
                if i==len(s1) and j==len(s2):
                    return 0
                else:
                    s=s2[j:] if i==len(s1) else s1[i:]
                    for i in s:
                        c+=ord(i)
                return c
            
            if dp[i][j]!=-1:
                return dp[i][j]
            s=0
            if s1[i]==s2[j]:
                s=tra(i+1,j+1)
            else:
                s=min(ord(s1[i])+tra(i+1,j), ord(s2[j])+tra(i,j+1))
            
            dp[i][j]=s

            return dp[i][j]
        
        return tra(0,0)