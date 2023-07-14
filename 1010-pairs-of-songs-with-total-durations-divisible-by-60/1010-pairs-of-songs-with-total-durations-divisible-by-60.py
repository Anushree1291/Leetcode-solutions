class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp=[0]*60
        for i in time:
            dp[i%60]+=1
        
        ans=0
        for i in range(1,30):
            ans+=dp[i]*dp[60-i]
        
        ans+=int((dp[0]*(dp[0]-1))/2 + (dp[30]*(dp[30]-1))/2)
        return ans
        