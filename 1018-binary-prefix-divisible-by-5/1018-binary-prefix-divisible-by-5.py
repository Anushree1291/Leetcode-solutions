class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        t=[ False for _ in range(len(nums))]
        s=0
        if nums[0] == 0:
            s=0
            t[0] = True
        else: 
            s= 1
        for i in range(1, len(nums)):
            s = s*2+nums[i]
            if s%5==0:
                t[i]=True
        return t