class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        s=0
        for i in range(31):
            a=0
            for j in range(len(nums)):
                a+=(nums[j]>>i)&1
            s+=a*(len(nums)-a)
        return s