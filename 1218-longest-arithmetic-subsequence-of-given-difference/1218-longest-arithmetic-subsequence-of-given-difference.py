class Solution:
    def longestSubsequence(self, a: List[int], d: int) -> int:
        dp={}
        res=1
        for i in a:
            prev=dp.get(i-d,0)
            dp[i]=prev+1
            res=max(dp[i],res)
        return res