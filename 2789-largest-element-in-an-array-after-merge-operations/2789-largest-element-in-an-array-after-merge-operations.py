class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        s=0
        i=len(nums)-1
        m=0
        while i>-1:
            if nums[i]>s:
                s=0
            s+=nums[i]
            m=max(m,s)
            i-=1
        return m