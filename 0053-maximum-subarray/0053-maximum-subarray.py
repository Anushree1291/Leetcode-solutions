class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        m=nums[0]
        for i in nums:
            if sum<0:
                sum=i
            else:
                sum+=i
            print(i)
            m=max(m,sum)
        return m