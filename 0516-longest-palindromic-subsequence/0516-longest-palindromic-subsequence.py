class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        sr=s[::-1]
        a=[[None]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    a[i][j]=0
                elif sr[i-1]==s[j-1]:
                    a[i][j]=a[i-1][j-1]+1
                else:
                    a[i][j]=max(a[i-1][j],a[i][j-1])
        return a[-1][-1]