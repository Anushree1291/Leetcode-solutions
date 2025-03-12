class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n=0,0
        for i in nums:
            if i<0:
                n+=1
            if i>0: p+=1
        return max(n,p)