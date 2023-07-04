class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if (len(nums)==1):
            return nums[0]
        nums.sort()
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-2]!=nums[len(nums)-1]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-2):
            if(not( nums[i]==nums[i+1]) and not (nums[i]==nums[i-1])):
                return nums[i]
        return -1