class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        dp=[0]*(len(s)+1)
        ma=max(map(len,d))
        
        for i in range(1,len(s)+1):
            m=100
            for j in range(i-1,max(i-ma-1,-1),-1):
                e=0
                if s[j:i] not in d:
                    e=i-j
                m=min(e+dp[j],m)
            dp[i]=m
        
        return dp[len(s)]