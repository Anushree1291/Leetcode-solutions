class Solution:
    def change(self, a: int, coins: List[int]) -> int:
        
        dp=[0]*(a+1)
        dp[0]=1
        
        for c in coins:
            for i in range(c,a+1):
                dp[i]+=dp[i-c]
        
        return dp[a]