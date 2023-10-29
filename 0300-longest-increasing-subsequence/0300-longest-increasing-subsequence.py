import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a=[]
        a.append(nums[0])
        for i in range(len(nums)):
            if nums[i]>a[len(a)-1]:
                a.append(nums[i])
            else:
                l=bisect.bisect_left(a,nums[i])
                a[l]=nums[i]
        return len(a)
            