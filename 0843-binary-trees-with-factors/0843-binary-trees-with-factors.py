class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        dp={}
        m=1000000007
        res=0
        a.sort()
        for i in range(0,len(a)):
            dp[a[i]]=1
            for j in range(0,i):
                if a[i]%a[j]==0:
                    dp[a[i]]=(dp[a[i]]+dp[a[j]]*dp.get(a[i]//a[j],0))%m
            res=(res+dp[a[i]])%m
        return res