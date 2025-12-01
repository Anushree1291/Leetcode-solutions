class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d=0
        t=0
        divisors.sort()
        for i in range(len(divisors)):
            s=0
            for j in range(len(nums)):
                if nums[j]%divisors[i] ==0:
                    s+=1
            if s>d : 
                d=s
                t=divisors[i]
        return t