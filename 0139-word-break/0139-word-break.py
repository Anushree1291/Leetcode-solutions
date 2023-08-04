class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        ma=max(map(len,wordDict))
        #print(ma)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i-1,max(i-ma-1,-1),-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[len(s)]