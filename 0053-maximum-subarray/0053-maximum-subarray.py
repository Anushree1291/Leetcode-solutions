class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=m=nums[0]
        for i in range(1,len(nums)):
            s=max(nums[i],s+nums[i])
            m=max(m,s)
        return m