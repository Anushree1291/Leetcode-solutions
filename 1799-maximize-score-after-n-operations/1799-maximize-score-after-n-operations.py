class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m={():0}
        
        def dfs(num):
            if tuple(num) in m:
                return m[tuple(num)]
            n=len(num)
            res=0
            for i in range(n-1):
                for j in range(i+1,n):
                    num2=num.copy()
                    num2.remove(num[i])
                    num2.remove(num[j])
                    t=(n//2)*math.gcd(num[i],num[j])+dfs(num2)
                    
                    res=max(res,t)
            
            m[tuple(num)]=res
            
            return res
        
        return dfs(nums)